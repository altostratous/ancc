from unittest import TestCase

import os

from grammar.models import Literal
from parser.models import Parser
from parser.utils import create_transition_diagram, get_all_literals_from_non_terminals
from scanner.scanner import Scanner
from ui.manage import BASE_DIR


class TestParser(TestCase):
    def test_success_order(self):

        class OrderLoggerParser(Parser):

            def __init__(self, state_machines, start_state, scanner):
                super().__init__(state_machines, start_state, scanner)
                self.non_terminals_in_order = []

            def parsed(self, parsed_state):
                self.non_terminals_in_order.append(parsed_state.non_terminal.text)

        with open(os.path.join(BASE_DIR, 'resources/src/predictable_grammar.txt')) as grammar_file:
            non_terminals = Literal.parse(grammar_file)
            all_literals = get_all_literals_from_non_terminals(non_terminals)
            start, states = create_transition_diagram(non_terminals)
            parser = OrderLoggerParser(
                states, start,
                Scanner(
                    open(os.path.join(BASE_DIR, 'resources/test/code/hello_world.nc')).read(),
                    all_literals
                )
            )
            parser.parse()
            parsed_non_terminals = parser.non_terminals_in_order

            self.assertListEqual(parsed_non_terminals, [
                '',
                '',
                '',
                '',
                '',
                '',
                '',
            ])
