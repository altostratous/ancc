import os
from copy import copy

from grammer.models import Literal


def dfs(first, literal, mark):
    mark[literal] = 1
    for rule in literal.rules:
        if len(rule) and not rule[0].is_terminal:
            if not rule[0] in mark:
                if not dfs(first, rule[0], mark):
                    return False
            elif rule[0] == first:
                return False
    return True


def check_left_recursion(literals):
    out = []
    for i, literal in enumerate(literals):
        mark = {}
        if not dfs(literal, literal, mark):
            print("Left recursion found in", literal)
            out += [literal]
    return out


def resolve_left_recursion_simple(literals, bad_literals):
    from src.grammer.models import Literal

    for bt in bad_literals:
        index = literals.index(bt)
        rules_1 = [rule[1:] for rule in bt.rules if rule[0] == bt]
        rules_2 = [rule for rule in bt.rules if rule[0] != bt]
        new_literal = Literal(bt.text + '-prime')
        bt.rules = [rule2 + [new_literal] for rule2 in rules_2]
        new_literal.rules = [rule1 + [new_literal] for rule1 in rules_1] + [[]]
        literals.insert(index + 1, new_literal)
    return literals


def rule_to_str(rule):
    if not rule:
        return 'ε'
    return ' '.join([l.text for l in rule])


def print_to_file(literals, filename):
    with open(filename, "w") as f:
        for i, literal in enumerate(literals):
            f.write("{}. {} → ".format(i+1, literal.text) + " | ".join([rule_to_str(rule) for rule in literal.rules]) + "\n")


def requires_factorization(grammar):
    for non_terminal in grammar:
        for first_literal in non_terminal.rules:
            for second_literal in non_terminal.rules:
                if first_literal is second_literal:
                    continue
                if len(os.path.commonprefix([first_literal, second_literal])) > 0:
                    return True
    return False


def factorize(grammar):
    # only works for factorizations shared among all rules of the non terminal
    counter = 0
    new_grammar = copy(grammar)
    for non_terminal in grammar:
        counter += 1
        if len(non_terminal.rules) <= 1:
            continue
        prefix = os.path.commonprefix(non_terminal.rules)
        if len(prefix) > 0:
            new_non_terminal = Literal(
                'rest-of-' + non_terminal.text,
                [rule[len(prefix):] for rule in non_terminal.rules]
            )
            non_terminal.rules = [prefix + [new_non_terminal]]
            new_grammar.insert(counter, new_non_terminal)
            counter += 1
    return new_grammar
