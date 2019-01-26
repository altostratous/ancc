class Literal:
    CONVENTIONS = {
        'stmt': 'statement',
        'addop': 'additive operation',
        'fun': 'function',
        'param': 'parameter',
        'relop': 'relative operation',
        'expr': 'expression',
        'arg': 'argument',
        'prime': '',
        'rest': '',
        'NUM': 'number',
        'RELOP': 'relative operator',
        'ID': 'identifier',
        'int': 'integer',
        'EOF': 'end of file',
        ',': '`,`',
        '(': '`(`',
        ')': '`)`',
        '{': '`{`',
        '}': '`}`',
        ';': '`;`',
        '[': '`,`',
        ']': '`,`',
        '+': '`,`',
        '*': '`*`',
    }

    def __init__(self, text, rules=None):
        self.text = text
        self.rules = rules

    def __str__(self):
        return self.text

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return self.text.__lt__(other.text)

    def __cmp__(self, other):
        return self.text.__cmp__(other.text)

    @property
    def is_terminal(self):
        return self.rules is None

    @property
    def is_action(self):
        return False

    @property
    def verbose_name(self):
        if self.text == '-':
            return '`-`'
        parts = self.text.split('-')
        result = ''
        for part in parts:
            result += ' '
            if part in Literal.CONVENTIONS:
                result += Literal.CONVENTIONS[part]
            else:
                result += part
        return result[1:]

    @staticmethod
    def parse(raw_grammar_file):
        literals_map = {'ε': Literal('ε')}
        list_of_non_terminals = []
        for line in raw_grammar_file:
            line = line.replace('\n', '')
            left_hand_side_text, right_hand_sides_text = [side.strip() for side in line.split('→')]
            left_hand_side_text = left_hand_side_text.split('.')[-1][1:]
            list_of_list_of_right_hand_side_texts = [
                [
                    literal_text.strip() for literal_text in text.strip().split(' ')
                ] for text in right_hand_sides_text.split('|')
            ]
            if left_hand_side_text not in literals_map:
                literals_map[left_hand_side_text] = Literal.create(left_hand_side_text)
            list_of_non_terminals.append(literals_map[left_hand_side_text])
            for list_of_right_hand_side_texts in list_of_list_of_right_hand_side_texts:
                for literal_text in list_of_right_hand_side_texts:
                    if literal_text not in literals_map:
                        literals_map[literal_text] = Literal.create(literal_text)
                        if literals_map[literal_text].is_action:
                            list_of_non_terminals.append(literals_map[literal_text])
            literals_map[left_hand_side_text].rules = [
                [
                    literals_map[rule_literal] for rule_literal in right_hand_side_rule_texts
                ] if right_hand_side_rule_texts != ['ε'] else [] for right_hand_side_rule_texts in
                list_of_list_of_right_hand_side_texts
            ]

        return list_of_non_terminals

    @staticmethod
    def create(left_hand_side_text):
        from generator import actions
        if not left_hand_side_text.startswith('#'):
            return Literal(left_hand_side_text)
        action_class_name = left_hand_side_text.replace('#', '') + 'Action'
        action_class = getattr(actions, action_class_name)
        return action_class(left_hand_side_text)


class DataType(object):
    INTEGER = 'int'
    VOID = 'void'


class DeclarationType(object):
    ARRAY = 'array'
    FUNCTION = 'function'
    VARIABLE = 'variable'


class Token(object):

    def __init__(self, text, attribute, literal, data_type=None, declaration_type=None):
        super(Token, self).__init__()
        self.text = text
        self.attribute = attribute
        self.literal = literal
        self.data_type = data_type
        self.declaration_type = declaration_type

    def __eq__(self, o) -> bool:
        if o is None:
            return False
        return o.text == self.text and o.attribute == self.attribute

    def __str__(self) -> str:
        return 'Token(`{}`, {})'.format(self.text, self.attribute)

    def __repr__(self) -> str:
        return str(self)
