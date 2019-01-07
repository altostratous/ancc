from collections import OrderedDict
from unittest import TestCase

from os import path

from grammer.tokens import Token
from parser import Scanner

from scanner.scanner import RESERVED_WORDS


class TestScanner(TestCase):

    def test_comment(self):
        comment_file = open(path.join('resources', 'test', 'code', 'comment.nc'))
        scanner = Scanner(comment_file.read())
        self.assertEqual(scanner.get_next_token().text, 'EOF')

    def test_key_words(self):
        for reserved_word in RESERVED_WORDS:
            scanner = Scanner(reserved_word)
            self.assertEqual(scanner.get_next_token().text, reserved_word)

    def test_num_and_id(self):

        test_vector = OrderedDict({
            # NUM
            '95': Token('NUM', 95),
            '328': Token('NUM', 328),
            '+98': Token('NUM', 98),
            '-025': Token('NUM', -25),
            # ID
            'SomeID': Token('ID', 0),  # the index in symbol table
            'Zed56': Token('ID', 0)
        })

        for lexeme in test_vector.keys():
            self.assertEqual(
                Scanner(lexeme).get_next_token(),
                test_vector[lexeme],
                'Scanner failed to parse `{}` as {}'.format(lexeme, test_vector[lexeme])
            )

    def test_additive_expression_sense(self):
        scanner = Scanner('five = -145+theID+5+variable')
        self.assertEqual(scanner.get_next_token(), Token('ID', 0))
        self.assertEqual(scanner.get_next_token(), Token('=', None))
        self.assertEqual(scanner.get_next_token(), Token('NUM', -145))
        self.assertEqual(scanner.get_next_token(), Token('+', None))
        self.assertEqual(scanner.get_next_token(), Token('ID', 1))
        self.assertEqual(scanner.get_next_token(), Token('+', None))
        self.assertEqual(scanner.get_next_token(), Token('NUM', 5))
        self.assertEqual(scanner.get_next_token(), Token('+', None))
        self.assertEqual(scanner.get_next_token(), Token('ID', 3))
