import os
import sys
import subprocess
from os import path

from grammar.models import Literal

BASE_DIR = path.dirname(os.path.dirname(os.path.dirname(__file__)))


def generate():
    from grammar.utils import check_left_recursion, resolve_left_recursion_simple, print_to_file, factorize, \
        compute_first, requires_factorization, compute_follow

    new_grammar = current_grammar = Literal.parse(open(os.path.join(BASE_DIR, 'resources/src/raw_grammar.txt')))
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
    print_to_file(current_grammar, os.path.join(BASE_DIR, 'resources/src/predictable_grammar.txt'))
    print("Now grammar is predictable.")

    first = compute_first(current_grammar)
    follow = compute_follow(current_grammar, first)
    print("Computed first and follow sets.")

    with open(path.join(BASE_DIR, 'doc/README.md'), 'w') as doc_file:
        with open(path.join(BASE_DIR, 'resources/src/raw_grammar.txt')) as raw_grammar_file:
            with open(path.join(BASE_DIR, 'resources/src/recursion_free_grammar.txt')) as recursion_free_grammar_file:
                with open(path.join(BASE_DIR, 'resources/src/predictable_grammar.txt')) as predictable_grammar_file:
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
                        '## Predictable Grammar\n',
                        '```\n',
                    ])
                    for line in predictable_grammar_file:
                        doc_file.write(line)

                    doc_file.writelines([
                        '```\n',
                        '## First and Follow\n'
                        '|Non-terminal|First|Follow|\n'
                        '|:----------:|:---:|:----:|\n'
                    ])

                    for non_terminal in first.keys():
                        doc_file.writelines([
                            '|{}|{}|{}|\n'.format(
                                non_terminal.text,
                                ' '.join(['ε' if literal == () else literal.text for literal in first[non_terminal]]),
                                ' '.join(['ε' if literal == () else literal.text for literal in follow[non_terminal]])
                            ),
                        ])


def test():
    subprocess.run(['python3.5', '-m', 'unittest', 'test_scanner'])


if __name__ == "__main__":

    if sys.argv[1] == 'generate':
        generate()
    elif sys.argv[1] == 'test':
        test()
    else:
        print('No such command `{}`.'.format(sys.argv[1]))
