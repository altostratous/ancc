import os

from src.grammer.utils import check_left_recursion, resolve_left_recursion_simple, print_to_file, \
    compute_first

RESOURCES_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

class Literal:
    def __init__(self, text, rules=None):
        self.text = text
        self.rules = rules

    def __str__(self):
        return self.text

    def __repr__(self):
        return str(self)

    @property
    def is_terminal(self):
        return self.rules is None

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
                ] if right_hand_side_rule_texts != ['ε'] else [] for right_hand_side_rule_texts in list_of_list_of_right_hand_side_texts
            ]

        return list_of_non_terminals


if __name__ == "__main__":
    l = Literal.parse(open(os.path.join(RESOURCES_DIR, 'resources/src/raw_grammer.txt')))
    while True:
        bl = check_left_recursion(l)
        if not bl:
            break
        new_grammar = resolve_left_recursion_simple(l, bl)
        print_to_file(new_grammar, (os.path.join(RESOURCES_DIR, 'resources/src/raw_grammer2.txt')))
        l = new_grammar
    print("Left recursion resolved.")
    x=compute_first(l)
    print(x)