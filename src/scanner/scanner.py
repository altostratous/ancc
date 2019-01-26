import string

from grammar.models import Token, DataType
from scanner.errors import DuplicateDeclaration, UndefinedIDError

RESERVED_WORDS = ['int', 'void', 'continue', 'break', 'if', 'else', 'while', 'return', 'switch', 'case', 'default']

SINGLE_CHARACTERS = [';', ',', '[', ']', '{', '}', '(', ')', ':', '*']


class Scanner:
    def __init__(self, input_string, literals):
        self.literals = dict([(literal.text, literal) for literal in literals])
        self.input = input_string
        self.index = 0
        self.len = len(input_string)
        self.prev_token = None
        self.first_free_memory = 0
        self.symbol_table = [{'output': Token('ID', 0, self.literals['ID'], DataType.VOID)}]
        self.malloc(1)  # reserve for output function

    def summary(self):
        result = ''
        index = self.index - 2
        while index >= 0 and self.input[index] != '\n':
            result = self.input[index] + result
            index -= 1
        result += '>'
        index = self.index - 1
        while index < self.len and self.input[index] != '\n':
            result += self.input[index]
            index += 1
        return result

    def malloc(self, size=1):
        address = self.first_free_memory
        self.first_free_memory += size
        return address

    def get_symbol_token(self, symbol_text):
        for scope_table in reversed(self.symbol_table):
            if symbol_text in scope_table:
                return scope_table[symbol_text]
        raise UndefinedIDError(symbol_text, self)

    def get_symbol_address(self, symbol_text):
        return self.get_symbol_token(symbol_text).attribute

    def get_token_by_address(self, address):
        for scope in self.symbol_table:
            for token in scope.values():
                if token.attribute == address:
                    return token

    def return_token(self, text, attr):
        data_type = None
        if self.prev_token is not None:
            if self.prev_token.text in ['void', 'int']:
                data_type = self.prev_token.text
        t = Token(text, attr, self.literals[text], data_type)
        self.prev_token = t
        assert isinstance(t, Token)
        return t

    def get_next_token(self, scope=0):

        assert scope <= len(self.symbol_table), "{} {}".format(scope, len(self.symbol_table))
        if scope == len(self.symbol_table):
            self.symbol_table.append({'output': self.symbol_table[0]['output']})

        self.symbol_table = self.symbol_table[0: scope + 1]

        def digit():
            digit_string = ""
            while self.index < self.len and self.input[self.index] in string.digits:
                digit_string += self.input[self.index]
                self.index += 1
            if digit_string == "":
                return "EXP"
            return int(digit_string)

        while True:
            while self.index < self.len and self.input[self.index] in string.whitespace:
                self.index += 1
            if self.len == self.index:
                self.index += 1
                return self.return_token('EOF', None)
            if self.len < self.index:
                return None
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

        if next_char in SINGLE_CHARACTERS:
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
            if self.prev_token and self.prev_token.text in ['int', 'void']:
                if st in self.symbol_table[scope]:
                    raise DuplicateDeclaration(st, *self.line_and_column())
                self.symbol_table[scope][st] = self.return_token('ID', self.malloc())
            return self.return_repeated_token(st)
        if next_char in string.digits:
            self.index -= 1
            return self.return_token('NUM', digit())
        if next_char in ['+', '-']:
            if self.prev_token is None or self.prev_token.text not in [']', ')', 'NUM', 'ID']:
                m = -1 if next_char == '-' else +1
                return self.return_token('NUM', m * digit())
            else:
                return self.return_token(next_char, None)
        assert False

    def line_and_column(self):
        line = 1
        column = 1
        for i in range(0, min(self.index, len(self.input))):
            column += 1
            if self.input[i] == '\n':
                line += 1
                column = 0
        return line, column

    def return_repeated_token(self, param):
        token = self.get_symbol_token(param)
        self.prev_token = token
        if not isinstance(token, Token):
            assert False
        return token
