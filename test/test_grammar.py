import os
from unittest import TestCase

from grammar.models import Literal
from grammar.utils import compute_non_terminals_firsts, compute_non_terminals_follows, check_predictability
from core.defines import BASE_DIR


class TestUtilities(TestCase):
    def test_first_follow(self):
        opened_file = open(os.path.join(BASE_DIR, 'resources', 'test', 'grammar', 'complex.txt'))
        non_terminals = Literal.parse(opened_file)
        literals_map = {}
        for non_terminal in non_terminals:
            literals_map[non_terminal.text] = non_terminal
            for rule in non_terminal.rules:
                for literal in rule:
                    literals_map[literal.text] = literal

        first = compute_non_terminals_firsts(non_terminals)
        follow = compute_non_terminals_follows(non_terminals, first)

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

        opened_file.close()


class TestGrammar(TestCase):
    def test_predictability(self):
        with open(os.path.join(BASE_DIR, 'resources', 'src', 'predictable_grammar.txt')) as grammar_file:
            grammar = Literal.parse(grammar_file)
            first = compute_non_terminals_firsts(grammar)
            self.assertTrue(check_predictability(
                grammar, first, compute_non_terminals_follows(grammar, first)
            ))
