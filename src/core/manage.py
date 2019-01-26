import os
import sys
import platform
import subprocess
import traceback
from collections import OrderedDict
from os import path

from core.defines import BASE_DIR
from grammar.models import Literal
from grammar.utils import check_predictability
from parser.models import Parser
from parser.utils import create_transition_diagram, print_diagram, escape, get_all_literals_from_non_terminals
from scanner.models import Scanner


def generate():
    from grammar.utils import check_left_recursion, resolve_left_recursion_simple, print_to_file, factorize, \
        compute_non_terminals_firsts, requires_factorization, compute_non_terminals_follows

    with open(os.path.join(BASE_DIR, 'resources/src/raw_grammar.txt')) as file:
        new_grammar = current_grammar = Literal.parse(file)

    while True:
        bad_literals = check_left_recursion(current_grammar)
        if not bad_literals:
            break
        new_grammar = resolve_left_recursion_simple(current_grammar, bad_literals)
        current_grammar = new_grammar

    print_to_file(new_grammar, os.path.join(BASE_DIR, 'resources/src/recursion_free_grammar.txt'))
    print("Left recursion resolved.")

    while requires_factorization(current_grammar):
        current_grammar = factorize(current_grammar)
        print("Factorized one time.")
    print_to_file(current_grammar, os.path.join(BASE_DIR, 'resources/src/partially_factored_grammar.txt'))

    with open(os.path.join(BASE_DIR, 'resources/src/predictable_grammar.txt')) as file:
        current_grammar = Literal.parse(file)

    first = OrderedDict(compute_non_terminals_firsts(current_grammar))
    follow = OrderedDict(compute_non_terminals_follows(current_grammar, first))
    print("Computed first and follow sets.")
    check_predictability(current_grammar, first, follow)

    start_state, state_machines = create_transition_diagram(current_grammar)

    with open(path.join(BASE_DIR, 'doc/README.md'), 'w') as doc_file:
        with open(path.join(BASE_DIR, 'resources/src/raw_grammar.txt')) as raw_grammar_file:
            with open(path.join(BASE_DIR, 'resources/src/recursion_free_grammar.txt')) as recursion_free_grammar_file:
                with open(path.join(
                        BASE_DIR,
                        'resources/src/partially_factored_grammar.txt')) as partially_factored_grammar_file:
                    with open(path.join(
                            BASE_DIR,
                            'resources/src/predictable_grammar.txt')) as predictable_grammar_file:
                        doc_file.writelines([
                            '# ANCC Automatically Generated Documentation\n',
                            '## Raw Grammar\n',
                            '```\n',
                        ])
                        for line in raw_grammar_file:
                            doc_file.write(line)
                        doc_file.writelines([
                            '```\n',
                            '## Recursion Free Grammar\n',
                            '```\n',
                        ])
                        for line in recursion_free_grammar_file:
                            doc_file.write(line)

                        doc_file.writelines([
                            '```\n',
                            '## Partially Factored Grammar\n',
                            '```\n',
                        ])
                        for line in partially_factored_grammar_file:
                            doc_file.write(line)

                        doc_file.writelines([
                            '```\n',
                            '## Predictable Grammar\n',
                            '```\n',
                        ])
                        for line in predictable_grammar_file:
                            doc_file.write(escape(line))

                        doc_file.writelines([
                            '\n',
                            '```\n',
                            '## State Diagram\n',
                            '```\n',
                        ])
                        print_diagram(state_machines, doc_file)

                        doc_file.writelines([
                            '```\n',
                            '## First and Follow\n'
                            '|Non-terminal|First|Follow|\n'
                            '|:----------:|:---:|:----:|\n'
                        ])

                        for non_terminal in sorted(first.keys()):
                            doc_file.writelines([
                                '|{}|{}|{}|\n'.format(
                                    non_terminal.text,
                                    ' '.join(sorted([
                                        'ε' if literal == () else literal.text for literal in first[non_terminal]
                                    ])),
                                    ' '.join(sorted([
                                        'ε' if literal == () else literal.text for literal in follow[non_terminal]
                                    ]))
                                ),
                            ])


def test():
    subprocess.run(['python3', '-m', 'unittest', 'integration_test'])
    subprocess.run(['python3', '-m', 'unittest', 'test_grammar'])
    subprocess.run(['python3', '-m', 'unittest', 'test_parser'])
    subprocess.run(['python3', '-m', 'unittest', 'test_scanner'])


def print_usage():
    print("Usage:")
    print("\tancc <nc code file> <output path> [--no-run]")
    print("\tancc test")
    print("\tancc generate")


def compile_nc_code(input_string):
    with open(os.path.join(BASE_DIR, 'resources/src/predictable_grammar.txt')) as grammar_file:
        non_terminals = Literal.parse(grammar_file)
        all_literals = get_all_literals_from_non_terminals(non_terminals)
        start, states = create_transition_diagram(non_terminals)
        parser = Parser(
            states, start,
            Scanner(
                input_string,
                all_literals
            )
        )
        errors = parser.parse()
        if errors:
            for error in errors:
                print(sys.stderr, error)
            return ''
        return str(parser.program)


if __name__ == "__main__":

    if sys.argv[1] == 'generate':
        generate()
    elif sys.argv[1] == 'test':
        test()
    else:
        if len(sys.argv) not in [3, 4]:
            print_usage()
            exit(1)
        try:
            output_code = compile_nc_code(open(sys.argv[1]).read())
            open(sys.argv[2], mode='w').write(output_code)
            if len(sys.argv) == 4:
                if sys.argv[3] == '--no-run':
                    exit(0)
                else:
                    print("Unknown argument {}".format(sys.argv[3]))
                    print_usage()
            open("output.txt", mode='w').write(output_code)
            if platform.system() == 'Darwin':
                os.system('bin/tester_mac.out')
            elif platform.system() == 'Linux':
                os.system('bin/tester_linux.out')
            else:
                print(sys.stderr, 'Unrecognized OS {}'.format(sys.platform.system()))
                exit(1)
        except Exception as exception:
            print(sys.stderr, "ANCC Unknown Error: " + str(exception))
            traceback.print_exc()
        finally:
            os.system('rm -f output.txt')

