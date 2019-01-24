from generator.program import Mnemonic, immval
from grammar.models import Literal


class Action(Literal):
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
        print(parser.lookahead_token.text)
        # assert parser.lookahead_token.text == '+' or parser.lookahead_token.text == '-'
        parser.semantic_stack += [parser.lookahead_token.text]


class AddOpAction(Action):
    def do(self, parser):
        if parser.semantic_stack[-2] == '+':
            parser.program.add_inst(Mnemonic.ADD, parser.semantic_stack[-1], parser.semantic_stack[-3])
        elif parser.semantic_stack[-2] == '-':
            parser.program.add_inst(Mnemonic.SUBTRACT, parser.semantic_stack[-1], parser.semantic_stack[-3])
        # else:
        #     assert 0, 'Either + or - must have been provided'
        parser.semantic_stack.pop()
        parser.semantic_stack.pop()
        parser.semantic_stack.pop()