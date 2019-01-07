def dfs(first, terminal, mark):
    mark[terminal] = 1
    for rule in terminal.rules:
        if len(rule) and not rule[0].is_terminal:
            if not rule[0] in mark:
                if not dfs(first, rule[0], mark):
                    return False
            elif rule[0] == first:
                return False
    return True


def check_left_recursion(terminals):
    out = []
    for i, terminal in enumerate(terminals):
        mark = {}
        if not dfs(terminal, terminal, mark):
            print("Left recursion found in", terminal)
            out += [terminal]
    return out


def resolve_left_recursion_simple(terminals, bad_terminals):
    from src.grammer.models import Literal

    for bt in bad_terminals:
        index = terminals.index(bt)
        rules_1 = [rule[1:] for rule in bt.rules if rule[0] == bt]
        rules_2 = [rule for rule in bt.rules if rule[0] != bt]
        new_terminal = Literal(bt.text + '-prime')
        bt.rules = [rule2 + [new_terminal] for rule2 in rules_2]
        new_terminal.rules = [rule1 + [new_terminal] for rule1 in rules_1] + [[]]
        terminals.insert(index + 1, new_terminal)
    return terminals


def rule_to_str(rule):
    if not rule:
        return 'ε'
    return ' '.join([l.text for l in rule])


def print_to_file(literals, filename):
    with open(filename, "w") as f:
        for i, literal in enumerate(literals):
            f.write("{}. {} → ".format(i+1, literal.text) + " | ".join([rule_to_str(rule) for rule in literal.rules]) + "\n")