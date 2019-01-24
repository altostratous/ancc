from generator.program import Mnemonic, immval
from grammar.models import Literal


class Action(Literal):
    def __init__(self, text):
        super().__init__(text, [[]])

    @property
    def is_action(self):
        return True

    def do(self, parser):
        pass


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


class PushRelOpAction(Action):
    def do(self, parser):
        assert parser.lookahead_token.text == 'RELOP'
        parser.semantic_stack += [parser.lookahead_token.attribute]


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


class RelOpAction(Action):
    def do(self, parser):
        tmp = parser.get_temp()
        if parser.semantic_stack[-2] == 'L':
            parser.program.add_inst(Mnemonic.LESS_THAN, parser.semantic_stack[-3], parser.semantic_stack[-1], tmp)
        elif parser.semantic_stack[-2] == 'E':
            parser.program.add_inst(Mnemonic.EQUALS, parser.semantic_stack[-3], parser.semantic_stack[-1], tmp)
        else:
            assert 0, 'Either < or == must have been provided'
        parser.semantic_stack.pop()
        parser.semantic_stack.pop()
        parser.semantic_stack.pop()
        parser.semantic_stack += [tmp]


class MultOpAction(Action):
    def do(self, parser):
        tmp = parser.get_temp()
        parser.program.add_inst(Mnemonic.MULTIPLY, parser.semantic_stack[-2], parser.semantic_stack[-1], tmp)
        parser.semantic_stack.pop()
        parser.semantic_stack.pop()
        parser.semantic_stack += [tmp]


class IfSaveAction(Action):
    def do(self, parser):
        parser.semantic_stack += [parser.program.pc]
        parser.program.add_fake_inst()


class IfJumpSaveAction(Action):
    def do(self, parser):
        # Jump
        parser.program.edit_inst(parser.semantic_stack.pop(), Mnemonic.JUMP_FALSE, parser.semantic_stack.pop(), parser.program.pc + 1)

        # Save
        parser.semantic_stack += [parser.program.pc]
        parser.program.add_fake_inst()


class IfJumpAction(Action):
    def do(self, parser):
        parser.program.edit_inst(parser.semantic_stack.pop(), Mnemonic.JUMP, parser.program.pc)
