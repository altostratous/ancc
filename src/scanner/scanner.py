import string

from src.grammer.tokens import Token

RESERVED_WORDS = ['int', 'void', 'continue', 'break', 'if', 'else', 'while', 'return', 'switch', 'case', 'default']

single_characters = [';', ',', '[', ']', '{', '}', '(', ')', ':', '*']


class Scanner:
    def __init__(self, input):
        self.input = input
        self.index = 0
        self.len = len(input)
        self.prev_token = None
        self.symbol_table = {}

    def return_token(self, text, attr):
        t = Token(text, attr)
        self.prev_token = t
        return t

    def get_next_token(self):
        def digit():
            st = ""
            while self.index < self.len and self.input[self.index] in string.digits:
                st += self.input[self.index]
                self.index += 1
            if st == "":
                return "EXP"
            return int(st)

        while True:
            if self.len == self.index:
                return self.return_token('EOF', None)
            next_char = self.input[self.index]
            self.index += 1
            if next_char == '/':
                if self.index < self.len and self.input[self.index] == '*':
                    self.index += 1
                    while self.index + 1 < self.len and not (
                            self.input[self.index == '*'] and self.input[self.index + 1] == '/'):
                        self.index += 1
                    self.index += 2
                    if self.index >= self.len:
                        return "EXP"
                else:
                    break
            else:
                break
        if next_char in single_characters:
            return self.return_token(next_char, None)
        if next_char == '<':
            return self.return_token('RELOP', 'L')
        if next_char == '=':
            if self.index < self.len and self.input[self.index] == '=':
                self.index += 1
                return self.return_token('RELOP', 'E')
            return self.return_token(next_char, None)
        if next_char in string.ascii_letters:
            st = next_char
            while self.index < self.len and self.input[self.index] in (string.ascii_letters + string.digits):
                st += self.input[self.index]
                self.index += 1
            if st in RESERVED_WORDS:
                return self.return_token(st, None)
            if st not in self.symbol_table:
                self.symbol_table[st] = len(self.symbol_table)
            return self.return_token('ID', self.symbol_table[st])
        if next_char in string.digits:
            self.index -= 1
            return self.return_token('NUM', digit())
        if next_char in ['+', '-']:
            if not self.prev_token is None and self.prev_token.text in [']', ')', 'NUM', 'ID']:
                m = -1 if next_char == '-' else +1
                return self.return_token('NUM', m * digit())
            else:
                return self.return_token(next_char, None)
