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
        for line in raw_grammar_file:
            line = line.replace('\n', '')
            left_hand_side, right_hand_side = line.split('→')
