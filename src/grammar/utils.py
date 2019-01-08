import os
from copy import copy

from grammar.models import Literal


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
def compute_follow(non_terminals, first):
    epsilon = ()
    follow = {x: set() for x in non_terminals}
    continue_computation = True
    while continue_computation:
        continue_computation = False
        for non_terminal in non_terminals:
            for rule in non_terminal.rules:
                for i in range(len(rule) - 1):
                    j = i + 1
                    first_literal, second_literal = rule[i], rule[j]
                    if first_literal.is_terminal:
                        continue
                    if second_literal.is_terminal:
                        follow[first_literal], continue_computation = inner_add(
                            follow[first_literal],
                            {second_literal},
                            continue_computation
                        )
                        continue
                    while True:
                        follow[first_literal], continue_computation = inner_add(
                            follow[first_literal],
                            first[second_literal] if not second_literal.is_terminal else {second_literal},
                            continue_computation
                        )

                        if second_literal.is_terminal or epsilon not in first[second_literal]:
                            break

                        assert epsilon in first[second_literal]

                        if j + 1 >= len(rule):
                            follow[first_literal], continue_computation = inner_add(
                                follow[first_literal],
                                follow[non_terminal],
                                continue_computation
                            )
                            break

                        j += 1
                        second_literal = rule[j]
                if len(rule) > 0 and not rule[len(rule) - 1].is_terminal:
                    follow[rule[len(rule) - 1]], continue_computation = inner_add(
                        follow[rule[len(rule) - 1]],
                        follow[non_terminal],
                        continue_computation
                    )

    for literal in follow.keys():
        if epsilon in follow[literal]:
            follow[literal].remove(epsilon)

    return follow


# we used http://hackingoff.com/compilers/predict-first-follow-set to verify our methods
def compute_first(non_terminals):
    first = {x: set() for x in non_terminals}

    while True:
        changed = False
        for literal in non_terminals:
            for rule in literal.rules:
                if not rule:
                    first[literal], changed = inner_add(first[literal], {()}, changed)
                    first[literal].add(())
                for i, sym in enumerate(rule):
                    if sym.is_terminal:
                        first[literal], changed = inner_add(first[literal], {sym}, changed)
                        break
                    else:
                        first[literal], changed = inner_add(first[literal], first[sym]-{()}, changed)
                        if not () in first[sym]:
                            break
                if i == len(rule):
                    first[literal], changed = inner_add(first[literal], {()}, changed)
        if not changed:
            break
    return first


def compute_first2(expressions, first):
    if not expressions:
        return set(())
    ans = set()
    for exp in expressions:
        if exp.is_terminal:
            return ans.union({exp})
        ans = ans.union(first[exp])
        if not () in first[exp]:
            return ans
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


def check_predictability(grammar, first):
    error = False
    for non_terminal in grammar:
        for i in range(len(non_terminal.rules)):
            if not non_terminal.rules[i]:
                continue
            for j in range(i+1, len(non_terminal.rules)):
                if not non_terminal.rules[j]:
                    continue
                f1 = compute_first2(non_terminal.rules[i], first)
                f2 = compute_first2(non_terminal.rules[j], first)
                if f1.intersection(f2):
                    f1 = compute_first2(non_terminal.rules[i], first)
                    f2 = compute_first2(non_terminal.rules[j], first)
                    error = True
                    print("Problem found; intersecting firsts between rules: {} → {} and {} → {}".format(non_terminal, rule_to_str(non_terminal.rules[i]), non_terminal, rule_to_str(non_terminal.rules[j])))
    if not error:
        print("All ok and predictable")