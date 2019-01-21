from parser.models import State
import sys


def print_dfa(q, out=sys.stdout):
    i = 0
    while i < len(q):
        print(q[i].full_repr(), file=out)
        # print(q[i].nexts)
        for _, next_state in q[i].nexts:
            if next_state not in q:
                q.append(next_state)
        i += 1


def print_diagram(state_machines, out=sys.stdout):
    for literal, state in state_machines.items():
        print(file=out)
        print(literal, file=out)
        print_dfa([state], out=out)


def create_transition_diagram(literals):
    state_machines = {}
    start_state = None

    for non_terminal in literals:
        start_state_1 = State(non_terminal)
        for rule in non_terminal.rules:
            current_state = start_state_1
            if not rule:
                new_state = State(non_terminal)
                current_state.nexts += [((), new_state)]
                new_state.is_success = True
                continue
            for lit in rule:
                new_state = State(non_terminal)
                current_state.nexts += [(lit, new_state)]
                current_state = new_state
            current_state.is_success = True
        if not state_machines:
            start_state = start_state_1
        state_machines[non_terminal] = start_state_1

    return start_state, state_machines


def get_all_literals_from_non_terminals(non_terminals):
    all_literals = set()
    for non_terminal in non_terminals:
        all_literals.add(non_terminal)
        for rule in non_terminal.rules:
            all_literals = all_literals.union(rule)
    return all_literals