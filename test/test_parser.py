from unittest import TestCase
import pprint

import os

from grammar.models import Literal
from parser.models import Parser
from parser.utils import create_transition_diagram, get_all_literals_from_non_terminals
from resources.test.parse_trees.easy2_pt import easy2_expected_parse_tree
from resources.test.parse_trees.easy_pt import easy_expected_parse_tree
from resources.test.parse_trees.final_pt import final_expected_parse_tree
from resources.test.parse_trees.hello_world_pt import hello_world_expected_parse_tree
from resources.test.parse_trees.if_while_pt import if_while_expected_parse_tree
from resources.test.parse_trees.switch_pt import switch_expected_parse_tree
from resources.test.parse_trees.test2_pt import test2_expected_parse_tree
from scanner.scanner import Scanner
from ui.manage import BASE_DIR


class TestParser(TestCase):
    test_cases = [['hello_world.nc', hello_world_expected_parse_tree, 'predictable_grammar_v1.txt'],
                  ['test2.nc', test2_expected_parse_tree, 'predictable_grammar_v1.txt'],
                  ['if_while.nc', if_while_expected_parse_tree, 'predictable_grammar_v2.txt'],
                  ['switch.nc', switch_expected_parse_tree, 'predictable_grammar_v2.txt'],
                  ['easy.nc', easy_expected_parse_tree, 'predictable_grammar_v2.txt'],
                  ['easy2.nc', easy2_expected_parse_tree, 'predictable_grammar_v3.txt'],
                  ['final.nc', final_expected_parse_tree, 'predictable_grammar_v3.txt'],
                ]
    maxDiff = None

    def test_success_order(self):
        for filename, expected_parse_tree, grammar_filename in TestParser.test_cases:

            with open(os.path.join(os.path.join(BASE_DIR, 'resources/test/grammar'), grammar_filename)) as grammar_file:
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
                    self.assertEqual(parse_tree[0], expected_parse_tree[0], "Error in " + filename)
                    self.assertListEqual(parse_tree[1], expected_parse_tree[1], "Error in " + filename)


class TestPanicMode(TestCase):

    test_cases = [
        # ['expression_error.nc', [('NUM', 'expression')], 'predictable_grammar_v2.txt'],
        ['function_declaration_error.nc',
         [(',', 'void-starting-param-list'), ('NUM', 'expression')],
         'predictable_grammar_v2.txt']
    ]

    def test_success_order(self):
        for filename, expected_parse_errors, grammar_filename in TestPanicMode.test_cases:

            with open(os.path.join(os.path.join(BASE_DIR, 'resources/test/grammar'), grammar_filename)) as grammar_file:
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
                    errors = parser.parse()
                    self.assertEqual(len(expected_parse_errors), len(errors))
                    for error in errors:
                        self.assertIn(
                            (error.lookahead.text, error.non_terminal.text), expected_parse_errors)
