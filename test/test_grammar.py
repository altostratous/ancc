import os
from unittest import TestCase

from grammar.models import Literal
from grammar.utils import compute_first, compute_follow
from ui.manage import BASE_DIR


class TestUtilities(TestCase):
    def test_first_follow(self):
        non_terminals = Literal.parse(open(os.path.join(BASE_DIR, 'resources', 'test', 'grammar', 'complex.txt')))
        literals_map = {}
        for non_terminal in non_terminals:
            literals_map[non_terminal.text] = non_terminal
            for rule in non_terminal.rules:
                for literal in rule:
                    literals_map[literal.text] = literal

        first = compute_first(non_terminals)
        follow = compute_follow(non_terminals, first)

        self.assertDictEqual(dict(first), {
            literals_map['s']: {literals_map['f']},
            literals_map['s-prime']: {literals_map['f']},
            literals_map['a']: {literals_map['f']},
            literals_map['b']: {()},
            literals_map['c']: {literals_map['f']},
            literals_map['d']: {()},
        })

        self.assertDictEqual(follow, {
            literals_map['s']: set(),
            literals_map['s-prime']: {literals_map['EOF']},
            literals_map['a']: {literals_map['f']},
            literals_map['b']: {literals_map['f']},
            literals_map['c']: {literals_map['EOF'], literals_map['f']},
            literals_map['d']: {literals_map['EOF']},
        })
