import string

from core.models import Token
from core.defines import DataType, DeclarationType, RESERVED_WORDS, SINGLE_CHARACTERS
from scanner.errors import DuplicateDeclaration, UndefinedIDError, LexicalError, NumberFormatError, SemanticError


class Scanner:
    def __init__(self, input_string, literals):
        self.literals = dict([(literal.text, literal) for literal in literals])
        self.input = input_string
        self.index = 0
        self.len = len(input_string)
        self.prev_token = None
        self.first_free_memory = 0
        self.symbol_table = [{'output': Token('ID', 0, self.literals['ID'], DataType.VOID, DeclarationType.FUNCTION, [Token('ID', -1, self.literals['ID'], DataType.INTEGER)])}]
        self.malloc(1)  # reserve for output function

    def summary(self):
        result = ''
        index = self.index - 1
        while index >= 0 and self.input[index] != '\n':
            result = self.input[index] + result
            index -= 1
        result += '<'
        index = self.index
        while index < self.len and self.input[index] != '\n':
            result += self.input[index]
            index += 1
        return result

    def malloc(self, size=1):
        if size <= 0:
            raise SemanticError('Array size must be a positive integer value', self)
        address = self.first_free_memory
        self.first_free_memory += size
        return address

    def find_symbol_token(self, symbol_text, scope=None):
        for i, scope_table in enumerate(reversed(self.symbol_table)):
            if scope is not None:
                if scope != len(self.symbol_table) - 1 - i:
                    continue
            if symbol_text in scope_table:
                return scope_table[symbol_text]

    def get_symbol_token(self, symbol_text):
        result = self.find_symbol_token(symbol_text)
        if result is None:
            raise UndefinedIDError(symbol_text, self)
        return result

    def get_symbol_address(self, symbol_text):
        return self.get_symbol_token(symbol_text).attribute

    def get_token_by_address(self, address):
        for scope in self.symbol_table:
            for token in scope.values():
                if token.attribute == address:
                    return token

    def return_token(self, text, attr, lexeme):
        data_type = None
        if self.prev_token is not None:
            if self.prev_token.text in ['void', 'int']:
                data_type = self.prev_token.text
        t = Token(text, attr, self.literals[text], data_type, lexeme=lexeme)
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
                raise NumberFormatError(self)
            return int(digit_string)

        while True:
            while self.index < self.len and self.input[self.index] in string.whitespace:
                self.index += 1
            if self.len == self.index:
                self.index += 1
                return self.return_token('EOF', None, '')
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
                        raise LexicalError("unexpected end of file.")
                else:
                    break
            else:
                break

        if next_char in SINGLE_CHARACTERS:
            return self.return_token(next_char, None, '')
        if next_char == '<':
            return self.return_token('RELOP', 'L', '')
        if next_char == '=':
            if self.index < self.len and self.input[self.index] == '=':
                self.index += 1
                return self.return_token('RELOP', 'E', '')
            return self.return_token(next_char, None, '')
        if next_char in string.ascii_letters:
            st = next_char
            while self.index < self.len and self.input[self.index] in (string.ascii_letters + string.digits):
                st += self.input[self.index]
                self.index += 1
            if st in RESERVED_WORDS:
                return self.return_token(st, None, st)
            if self.prev_token and self.prev_token.text in ['int', 'void']:
                if st in self.symbol_table[scope]:
                    raise DuplicateDeclaration(st, *self.line_and_column())
                self.symbol_table[scope][st] = self.return_token('ID', self.malloc(), st)
                self.analyze_semantics()
            return self.return_repeated_token(st)
        if next_char in string.digits:
            self.index -= 1
            return self.return_token('NUM', digit(), '')
        if next_char in ['+', '-']:
            if self.prev_token is None or self.prev_token.text not in [']', ')', 'NUM', 'ID']:
                m = -1 if next_char == '-' else +1
                return self.return_token('NUM', m * digit(), '')
            else:
                return self.return_token(next_char, None, '')
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

    def analyze_semantics(self):
        self.check_main()
        self.check_declaration_and_data_type_consistency()

    def check_main(self):
        main_token = self.find_symbol_token('main', 0)
        if main_token is None:
            return
        if main_token.data_type != DataType.VOID:
            raise SemanticError('main should be of type `void`', self)
        # TODO check main have (void) as args
        if main_token.declaration_type in {DeclarationType.VARIABLE, DeclarationType.ARRAY}:
            raise SemanticError('main function in the parent scope should be declared as a function', self)

    def check_declaration_and_data_type_consistency(self):
        for scope_table in self.symbol_table:
            for name, token in scope_table.items():
                if token.declaration_type is not None:
                    if token.declaration_type in {DeclarationType.VARIABLE, DeclarationType.ARRAY} and token.data_type != DataType.INTEGER:
                        raise SemanticError('variable {} should be of type `int`'.format(name), self)

