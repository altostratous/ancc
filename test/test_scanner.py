from collections import OrderedDict
from unittest import TestCase

from os import path
import os

from grammar.models import Literal, Token
from parser.utils import get_all_literals_from_non_terminals
from scanner.scanner import Scanner

from scanner.scanner import RESERVED_WORDS
from ui.manage import BASE_DIR


class TestScanner(TestCase):

    def setUp(self):
        with open(os.path.join(BASE_DIR, 'resources/src/predictable_grammar.txt')) as grammar_file:
            non_terminals = Literal.parse(grammar_file)
            self.all_literals = get_all_literals_from_non_terminals(non_terminals)

    def test_comment(self):
        with open(
            path.join(
                path.dirname(path.abspath(__file__)), '..', 'resources', 'test', 'code', 'comment.nc'
            )
        ) as comment_file:
            scanner = Scanner(comment_file.read(), self.all_literals)
        self.assertEqual(scanner.get_next_token().text, 'EOF')

    def test_key_words(self):
        for reserved_word in RESERVED_WORDS:
            scanner = Scanner(reserved_word, self.all_literals)
            self.assertEqual(scanner.get_next_token().text, reserved_word)

    def test_num_and_id(self):

        test_vector = OrderedDict({
            # NUM
            '95': self.get_token('NUM', 95),
            '328': self.get_token('NUM', 328),
            '+98': self.get_token('NUM', 98),
            '-025': self.get_token('NUM', -25),
            # ID
            'int SomeID': self.get_token('int', None),  # the index in symbol table
            'void SomeID': self.get_token('void', None)
        })

        for lexeme in test_vector.keys():
            self.assertEqual(
                Scanner(lexeme, self.all_literals).get_next_token(),
                test_vector[lexeme],
                'Scanner failed to parse `{}` as {}'.format(lexeme, test_vector[lexeme])
            )

    def test_additive_expression_sense(self):
        scanner = Scanner('int five; five = -145+five+5+five', self.all_literals)
        self.assertEqual(scanner.get_next_token(), self.get_token('int', None))
        self.assertEqual(scanner.get_next_token(), self.get_token('ID', 0))
        self.assertEqual(scanner.get_next_token(), self.get_token(';', None))
        self.assertEqual(scanner.get_next_token(), self.get_token('ID', 0))
        self.assertEqual(scanner.get_next_token(), self.get_token('=', None))
        self.assertEqual(scanner.get_next_token(), self.get_token('NUM', -145))
        self.assertEqual(scanner.get_next_token(), self.get_token('+', None))
        self.assertEqual(scanner.get_next_token(), self.get_token('ID', 0))
        self.assertEqual(scanner.get_next_token(), self.get_token('+', None))
        self.assertEqual(scanner.get_next_token(), self.get_token('NUM', 5))
        self.assertEqual(scanner.get_next_token(), self.get_token('+', None))
        self.assertEqual(scanner.get_next_token(), self.get_token('ID', 0))
        self.assertEqual(scanner.get_next_token(), self.get_token('EOF', None))

    def test_complex_expression(self):
        scanner = Scanner("""
            int y;
            int x;
            if (x == -125) {
                y = 125;
                x = +58; 
            } else 
                output(25);
        """, self.all_literals)

        self.assertEqual(scanner.get_next_token(), self.get_token('int', None))
        self.assertEqual(scanner.get_next_token(), self.get_token('ID', 0))
        self.assertEqual(scanner.get_next_token(), self.get_token(';', None))
        self.assertEqual(scanner.get_next_token(), self.get_token('int', None))
        self.assertEqual(scanner.get_next_token(), self.get_token('ID', 1))
        self.assertEqual(scanner.get_next_token(), self.get_token(';', None))
        self.assertEqual(scanner.get_next_token(), self.get_token('if', None))
        self.assertEqual(scanner.get_next_token(), self.get_token('(', None))
        self.assertEqual(scanner.get_next_token(), self.get_token('ID', 1))
        self.assertEqual(scanner.get_next_token(), self.get_token('RELOP', 'E'))
        self.assertEqual(scanner.get_next_token(), self.get_token('NUM', -125))
        self.assertEqual(scanner.get_next_token(), self.get_token(')', None))
        self.assertEqual(scanner.get_next_token(), self.get_token('{', None))
        self.assertEqual(scanner.get_next_token(), self.get_token('ID', 0))
        self.assertEqual(scanner.get_next_token(), self.get_token('=', None))
        self.assertEqual(scanner.get_next_token(), self.get_token('NUM', 125))
        self.assertEqual(scanner.get_next_token(), self.get_token(';', None))
        self.assertEqual(scanner.get_next_token(), self.get_token('ID', 1))
        self.assertEqual(scanner.get_next_token(), self.get_token('=', None))
        self.assertEqual(scanner.get_next_token(), self.get_token('NUM', 58))
        self.assertEqual(scanner.get_next_token(), self.get_token(';', None))
        self.assertEqual(scanner.get_next_token(), self.get_token('}', None))
        self.assertEqual(scanner.get_next_token(), self.get_token('else', None))
        self.assertEqual(scanner.get_next_token(), self.get_token('ID', -1))
        self.assertEqual(scanner.get_next_token(), self.get_token('(', None))
        self.assertEqual(scanner.get_next_token(), self.get_token('NUM', 25))
        self.assertEqual(scanner.get_next_token(), self.get_token(')', None))
        self.assertEqual(scanner.get_next_token(), self.get_token(';', None))
        self.assertEqual(scanner.get_next_token(), self.get_token('EOF', None))

    def get_token(self, text, attribute):
        for literal in self.all_literals:
            if literal.text == text:
                return Token(text, attribute, literal)
