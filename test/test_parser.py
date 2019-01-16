from unittest import TestCase

import os

from grammar.models import Literal
from grammar.utils import get_parse_tree_post_order
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

        with open(os.path.join(BASE_DIR, 'resources/test/grammar/predictable_grammar_v1.txt')) as grammar_file:
            with open(os.path.join(BASE_DIR, 'resources/test/code/hello_world.nc')) as hello_world_file:
                non_terminals = Literal.parse(grammar_file)
                all_literals = get_all_literals_from_non_terminals(non_terminals)
                start, states = create_transition_diagram(non_terminals)
                parser = OrderLoggerParser(
                    states, start,
                    Scanner(
                        hello_world_file.read(),
                        all_literals
                    )
                )
                parser.parse()
                parsed_non_terminals = parser.non_terminals_in_order

                simple_expression = {
                    'simple-expression': [
                        {
                            'additive-expression': [
                                {
                                    'term': [
                                        'factor',
                                        'term-prime'
                                    ]
                                },
                                'additive-expression-prime'
                            ]
                        },
                        'rest-of-simple-expression'
                    ]

                }

                id_expression = {
                    'id-expression': [
                        {
                            'id-simple-expression': [
                                {
                                    'id-additive-expression': [
                                        {
                                            'id-term': [
                                                {
                                                    'id-factor': [
                                                        {
                                                            'reference': [
                                                                {
                                                                    'call': [
                                                                        {
                                                                            'args': [
                                                                                {
                                                                                    'arg-list': [
                                                                                        {
                                                                                            'expression': [
                                                                                                simple_expression
                                                                                            ]
                                                                                        },
                                                                                        'arg-list-prime'

                                                                                    ]

                                                                                }
                                                                            ]
                                                                        }
                                                                    ]
                                                                }
                                                            ]
                                                        }
                                                    ]

                                                },
                                                'term-prime'
                                            ]
                                        },
                                        'additive-expression-prime'
                                    ]
                                },
                                'rest-of-simple-expression'
                            ]
                        }
                    ]
                }

                expected_parse_tree = {
                    'program': [
                        {
                            'declaration-list': [
                                {
                                    'declaration-list-prime': [
                                        'type-specifier',
                                        {
                                            'declaration': [
                                                {
                                                    'fun-declaration': [
                                                        {
                                                            'params': [
                                                                {
                                                                    'void-starting-param-list': [
                                                                        'rest-of-void-starting-param-list'
                                                                    ]
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            'compound-stmt': [
                                                                {
                                                                    'declaration-list': [
                                                                        'declaration-list-prime'
                                                                    ]
                                                                },
                                                                {
                                                                    'statement-list': [
                                                                        {
                                                                            'statement-list-prime': [
                                                                                {
                                                                                    'statement': [
                                                                                        {
                                                                                            'expression-stmt': [
                                                                                                {
                                                                                                    'expression': [
                                                                                                        id_expression
                                                                                                    ]
                                                                                                }
                                                                                            ]

                                                                                        }
                                                                                    ]
                                                                                },
                                                                                'statement-list-prime'
                                                                            ]
                                                                        }
                                                                    ]
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                },
                                            ]
                                        },
                                        'declaration-list-prime'
                                    ]
                                }
                            ]
                        }
                    ]
                }

                expected_post_order = [node for node in get_parse_tree_post_order(expected_parse_tree)]

                self.assertListEqual(parsed_non_terminals, expected_post_order)

