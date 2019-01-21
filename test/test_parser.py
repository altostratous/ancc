from unittest import TestCase
import pprint

import os

from grammar.models import Literal
from grammar.utils import get_parse_tree_post_order
from parser.models import Parser
from parser.utils import create_transition_diagram, get_all_literals_from_non_terminals
from resources.test.parse_trees.hello_world_pt import hello_world_expected_parse_tree
from resources.test.parse_trees.test2_pt import test2_expected_parse_tree
from scanner.scanner import Scanner
from ui.manage import BASE_DIR


class TestParser(TestCase):
    test_cases = [['hello_world.nc', hello_world_expected_parse_tree], ['test2.nc', test2_expected_parse_tree]]
    maxDiff = None

    def test_success_order(self):
        for filename, expected_parse_tree in TestParser.test_cases:

            with open(os.path.join(BASE_DIR, 'resources/test/grammar/predictable_grammar_v1.txt')) as grammar_file:
                with open(os.path.join(os.path.join(BASE_DIR, 'resources/test/code'), filename)) as test_file:
                    non_terminals = Literal.parse(grammar_file)
                    all_literals = get_all_literals_from_non_terminals(non_terminals)
                    start, states = create_transition_diagram(non_terminals)
                    parser = Parser(
                        states, start,
                        Scanner(
                            test_file.read(),
                            all_literals
                        )
                    )
                    parser.parse()
                    parsed_non_terminals = parser.tree
                    expected_post_order = [node for node in get_parse_tree_post_order(expected_parse_tree)]
                    # pprint.pprint(parser.tree)
                    self.assertListEqual(parsed_non_terminals, expected_post_order)
