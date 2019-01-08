import os

from grammar.models import Literal
from parser.models import State
from parser.utils import print_diagram


def create_transition_diagram(literals):

    state_machines = {}
    start_state = None

    for non_terminal in literals:
        start_state_1 = State()
        for rule in non_terminal.rules:
            current_state = start_state_1
            if not rule:
                current_state.nexts += [((), new_state)]
                new_state.is_success = True
                continue
            for lit in rule:
                new_state = State()
                current_state.nexts += [(lit, new_state)]
                current_state = new_state
            current_state.is_success = True
        if not state_machines:
            start_state = start_state_1
        state_machines[non_terminal] = start_state_1

    return start_state, state_machines


if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

    with open(os.path.join(BASE_DIR, 'resources/src/predictable_grammar.txt')) as f:
        literals = Literal.parse(f)
    start_state, state_machines = create_transition_diagram(literals)
    print_diagram(state_machines)
