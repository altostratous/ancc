import os

from grammar.models import Literal
from parser.models import State
from parser.utils import print_diagram



def parse(state_machines, start_state, scanner):
    current_state = start_state
    lookahead = scanner.get_next_token()





if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

    with open(os.path.join(BASE_DIR, 'resources/src/predictable_grammar.txt')) as f:
        literals = Literal.parse(f)
    start_state, state_machines = create_transition_diagram(literals)
    print_diagram(state_machines)
