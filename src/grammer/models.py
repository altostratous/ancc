class Literal:

    literals_map = {}

    def __init__(self, text, rules=None):
        self.text = text
        self.rules = rules

    @property
    def is_terminal(self):
        return self.rules is None

    @staticmethod
    def parse(raw_grammar_file):
        list_of_non_terminals = []
        for line in raw_grammar_file:
            line = line.replace('\n', '')
            left_hand_side_text, right_hand_sides_text = [side.strip() for side in line.split('→')]
            list_of_list_of_right_hand_side_texts = [
                [
                    literal_text.strip() for literal_text in text.strip().split(' ')
                ] for text in right_hand_sides_text.split('|')
            ]
            if left_hand_side_text not in Literal.literals_map:
                Literal.literals_map[left_hand_side_text] = Literal(left_hand_side_text)
            list_of_non_terminals.append(Literal.literals_map[left_hand_side_text])
            for list_of_right_hand_side_texts in list_of_list_of_right_hand_side_texts:
                for literal_text in list_of_right_hand_side_texts:
                    if literal_text not in Literal.literals_map:
                        Literal.literals_map[literal_text] = Literal(literal_text)
            Literal.literals_map[left_hand_side_text].rules = [
                [
                    Literal.literals_map[rule_literal] for rule_literal in right_hand_side_rule_texts
                ] for right_hand_side_rule_texts in list_of_list_of_right_hand_side_texts
            ]

        return list_of_non_terminals
