import os
from copy import copy

from grammar.models import Literal


def dfs(first, literal, mark):
    mark[literal] = 1
    for rule in literal.rules:
        if len(rule) and not rule[0].is_terminal and not rule[0].is_action:
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
    from grammar.models import Literal

    for bt in bad_literals:
        index = literals.index(bt)
        rules_1 = [rule[1:] for rule in bt.rules if len(rule) and rule[0] == bt]
        rules_2 = [rule for rule in bt.rules if not len(rule) or rule[0] != bt]
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
            f.write("{}. {} → ".format(i + 1, literal.text) + " | ".join(
                [rule_to_str(rule) for rule in literal.rules]) + "\n")


def inner_add(s1, s2, changed):
    u = s1.union(s2)
    if s1 != u:
        return u, True
    return u, changed


# we used http://hackingoff.com/compilers/predict-first-follow-set to verify our methods
def compute_non_terminals_follows(non_terminals, first):
    epsilon = ()
    follow = {x: set() for x in non_terminals}
    continue_computation = True
    while continue_computation:
        continue_computation = False
        for non_terminal in non_terminals:
            for rule in non_terminal.rules:
                for i in range(len(rule)):
                    first_literal = rule[i]
                    if first_literal.is_terminal or first_literal.is_action:
                        continue
                    first2 = compute_first_of_expression(rule[i + 1:], first)
                    follow[first_literal], continue_computation = inner_add(
                        follow[first_literal], first2 - {()},
                        continue_computation
                    )
                    if () in first2:
                        follow[first_literal], continue_computation = inner_add(
                            follow[first_literal], follow[non_terminal],
                            continue_computation
                        )

    for literal in follow.keys():
        assert epsilon not in follow[literal]

    return follow


# we used http://hackingoff.com/compilers/predict-first-follow-set to verify our methods
def compute_non_terminals_firsts(non_terminals):
    first = {x: set() for x in non_terminals}

    while True:
        changed = False
        for literal in non_terminals:
            for rule in literal.rules:
                if not rule:
                    first[literal], changed = inner_add(first[literal], {()}, changed)
                    first[literal].add(())
                must_include_epsilon = True
                for sym in rule:
                    if sym.is_action:
                        continue
                    if sym.is_terminal:
                        first[literal], changed = inner_add(first[literal], {sym}, changed)
                        must_include_epsilon = False
                        break
                    else:
                        first[literal], changed = inner_add(first[literal], first[sym]-{()}, changed)
                        if not () in first[sym]:
                            must_include_epsilon = False
                            break
                if must_include_epsilon:
                    first[literal], changed = inner_add(first[literal], {()}, changed)
        if not changed:
            break
    return first


def compute_first_of_expression(expressions, first):
    if not expressions:
        return {()}
    ans = set()
    for exp in expressions:
        if exp.is_action:
            continue
        if exp.is_terminal:
            return ans.union({exp}) - {()}
        ans = ans.union(first[exp])
        if not () in first[exp]:
            return ans - {()}
    return ans


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


def check_predictability(grammar, first, follow):
    error = False
    for non_terminal in grammar:
        for i in range(len(non_terminal.rules)):
            if not non_terminal.rules[i]:  # ε transition
                for other_rule in non_terminal.rules:
                    if not other_rule:
                        continue
                    if follow[non_terminal].intersection(compute_first_of_expression(other_rule, first)):
                        error = True
                        print("Problem found; intersecting {} first/follow between rules: {} → {} and {} → {}".format(
                            follow[non_terminal].intersection(compute_first_of_expression(other_rule, first)),
                            non_terminal, rule_to_str(non_terminal.rules[i]), non_terminal, rule_to_str(other_rule)))
                continue
            for j in range(i+1, len(non_terminal.rules)):
                if not non_terminal.rules[j]:
                    continue
                f1 = compute_first_of_expression(non_terminal.rules[i], first)
                f2 = compute_first_of_expression(non_terminal.rules[j], first)
                if f1.intersection(f2):
                    error = True
                    print("Problem found; intersecting {} firsts between rules: {} → {} and {} → {}".format(
                        f1.intersection(f2),
                        non_terminal, rule_to_str(non_terminal.rules[i]), non_terminal, rule_to_str(non_terminal.rules[j])))
    if not error:
        print("All ok and predictable")
    return not error
