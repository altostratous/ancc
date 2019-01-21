from unittest import TestCase
import pprint

import os

from grammar.models import Literal
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
                    parse_tree = parser.tree
                    # pprint.pprint(parser.tree)
                    self.assertEqual(parse_tree[0], expected_parse_tree[0], "Error in " + filename)
                    self.assertListEqual(parse_tree[1], expected_parse_tree[1], "Error in " + filename)

