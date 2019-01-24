from generator.program import Mnemonic, immval
from grammar.models import Literal


class Action(Literal):
    def __init__(self, text):
        super().__init__(text, [[]])

    @property
    def is_action(self):
        return True


class PrintAction(Action):
    def do(self, parser):
        parser.program.add_inst(Mnemonic.PRINT, parser.semantic_stack.pop())


class PushNumAction(Action):
    def do(self, parser):
        assert parser.lookahead_token.text == 'NUM'
        parser.semantic_stack += [immval(parser.lookahead_token.attribute)]


class PushAddOpAction(Action):
    def do(self, parser):
        assert parser.lookahead_token.text == '+'
        parser.semantic_stack += [parser.lookahead_token.text]


class PushSubOpAction(Action):
    def do(self, parser):
        assert parser.lookahead_token.text == '-'
        parser.semantic_stack += [parser.lookahead_token.text]


class AddOpAction(Action):
    def do(self, parser):
        tmp = parser.get_temp()
        if parser.semantic_stack[-2] == '+':
            parser.program.add_inst(Mnemonic.ADD, parser.semantic_stack[-3], parser.semantic_stack[-1], tmp)
        elif parser.semantic_stack[-2] == '-':
            parser.program.add_inst(Mnemonic.SUBTRACT, parser.semantic_stack[-3], parser.semantic_stack[-1], tmp)
        else:
            assert 0, 'Either + or - must have been provided'
        parser.semantic_stack.pop()
        parser.semantic_stack.pop()
        parser.semantic_stack.pop()
        parser.semantic_stack += [tmp]
