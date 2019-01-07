import copy


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
            f.write("{}. {} → ".format(i+1, literal.text) + " | ".join([rule_to_str(rule) for rule in literal.rules]) + "\n")


def compute_first(non_terminals):
    first = {x: set() for x in non_terminals}
    def inner_add(s1, s2, changed):
        u = s1.union(s2)
        if s1 != u:
            return u, True
        return u, changed

    while True:
        changed = False
        for literal in non_terminals:
            for rule in literal.rules:
                if not rule:
                    first[literal], changed = inner_add(first[literal], {()}, changed)
                    first[literal].add(())
                for sym in rule:
                    if sym.is_terminal:
                        first[literal], changed = inner_add(first[literal], {sym}, changed)
                        break
                    else:
                        first[literal], changed = inner_add(first[literal], first[sym], changed)
                        if not () in first[sym]:
                            break
        if not changed:
            break
    return first