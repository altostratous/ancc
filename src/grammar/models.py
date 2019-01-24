class Literal:
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
                literals_map[left_hand_side_text] = Literal(left_hand_side_text)
            list_of_non_terminals.append(literals_map[left_hand_side_text])
            for list_of_right_hand_side_texts in list_of_list_of_right_hand_side_texts:
                for literal_text in list_of_right_hand_side_texts:
                    if literal_text not in literals_map:
                        literals_map[literal_text] = Literal(literal_text)
            literals_map[left_hand_side_text].rules = [
                [
                    literals_map[rule_literal] for rule_literal in right_hand_side_rule_texts
                ] if right_hand_side_rule_texts != ['ε'] else [] for right_hand_side_rule_texts in
                list_of_list_of_right_hand_side_texts
            ]

        return list_of_non_terminals


class Token(object):

    def __init__(self, text, attribute, literal):
        super(Token, self).__init__()
        self.text = text
        self.attribute = attribute
        self.literal = literal

    def __eq__(self, o) -> bool:
        if o is None:
            return False
        return o.text == self.text and o.attribute == self.attribute

    def __str__(self) -> str:
        return 'Token(`{}`, {})'.format(self.text, self.attribute)

    def __repr__(self) -> str:
        return str(self)