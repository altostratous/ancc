from generator.program import Mnemonic, immval, indval
from grammar.models import Literal


class Action(Literal):
    def __init__(self, text):
        super().__init__(text, [[]])

    @property
    def is_action(self):
        return True

    def do(self, parser):
        pass


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
            parser.program.add_inst(Mnemonic.ADD, parser.semantic_stack[-3],
                                    parser.semantic_stack[-1], tmp)
        elif parser.semantic_stack[-2] == '-':
            parser.program.add_inst(Mnemonic.SUBTRACT, parser.semantic_stack[-3],
                                    parser.semantic_stack[-1], tmp)
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
            parser.program.add_inst(Mnemonic.LESS_THAN, parser.semantic_stack[-3],
                                    parser.semantic_stack[-1], tmp)
        elif parser.semantic_stack[-2] == 'E':
            parser.program.add_inst(Mnemonic.EQUALS, parser.semantic_stack[-3],
                                    parser.semantic_stack[-1], tmp)
        else:
            assert 0, 'Either < or == must have been provided'
        parser.semantic_stack.pop()
        parser.semantic_stack.pop()
        parser.semantic_stack.pop()
        parser.semantic_stack += [tmp]


class MultOpAction(Action):
    def do(self, parser):
        tmp = parser.get_temp()
        parser.program.add_inst(Mnemonic.MULTIPLY, parser.semantic_stack[-2],
                                parser.semantic_stack[-1], tmp)
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
        parser.program.edit_inst(parser.semantic_stack.pop(), Mnemonic.JUMP_FALSE,
                                 parser.semantic_stack.pop(), parser.program.pc + 1)

        # Save
        parser.semantic_stack += [parser.program.pc]
        parser.program.add_fake_inst()


class IfJumpAction(Action):
    def do(self, parser):
        parser.program.edit_inst(parser.semantic_stack.pop(), Mnemonic.JUMP, parser.program.pc)


class WhileLabelAction(Action):
    def do(self, parser):
        parser.program.add_inst(Mnemonic.JUMP, parser.program.pc + 2)

        # Save
        parser.break_stack += [parser.program.pc]
        parser.program.add_fake_inst()

        parser.continue_stack += [parser.program.pc]
        parser.semantic_stack += [parser.program.pc]


class WhileSaveAction(Action):
    def do(self, parser):
        parser.semantic_stack += [parser.program.pc]
        parser.program.add_fake_inst()


class WhileAction(Action):
    def do(self, parser):
        parser.program.edit_inst(parser.semantic_stack.pop(), Mnemonic.JUMP_FALSE,
                                 parser.semantic_stack.pop(), parser.program.pc + 1)
        parser.program.add_inst(Mnemonic.JUMP, parser.semantic_stack.pop())
        parser.program.edit_inst(parser.break_stack.pop(), Mnemonic.JUMP, parser.program.pc)
        parser.continue_stack.pop()


class SwitchSaveAction(Action):
    def do(self, parser):
        parser.program.add_inst(Mnemonic.JUMP, parser.program.pc + 2)

        # Save
        parser.semantic_stack += [parser.program.pc]
        parser.program.add_fake_inst()

        parser.semantic_stack += [parser.program.pc]
        parser.program.add_fake_inst()
        parser.program.add_fake_inst()
        parser.program.add_fake_inst()
        parser.program.add_fake_inst()
        parser.program.add_fake_inst()

        parser.semantic_stack += [[]]
        parser.semantic_stack += [0]  # Whether we have default or not


class CaseInsertAction(Action):
    def do(self, parser):
        assert parser.lookahead_token.text == 'NUM'
        parser.semantic_stack[-2].append((parser.lookahead_token.attribute, parser.program.pc))


class DefaultInsertAction(Action):
    def do(self, parser):
        assert parser.semantic_stack[-1] == 0
        parser.semantic_stack[-1] = 1


class SwitchAction(Action):
    def do(self, parser):
        l = parser.semantic_stack[-2]
        min1, max1 = max(l), min(l)
        l = map(lambda x: x - min1, l)
        max1 -= min1
        addr = parser.scanner.malloc(max1)


class PushIDAction(Action):
    def do(self, parser):
        assert parser.lookahead_token.text == 'ID'
        parser.semantic_stack += [parser.lookahead_token.attribute]


class AssignAction(Action):
    def do(self, parser):
        parser.program.add_inst(Mnemonic.ASSIGN, parser.semantic_stack.pop(),
                                parser.semantic_stack[-1])


class PopIDAction(Action):
    def do(self, parser):
        parser.semantic_stack.pop()


class BreakAction(Action):
    def do(self, parser):
        parser.program.add_inst(Mnemonic.JUMP, parser.break_stack[-1])


class ContinueAction(Action):
    def do(self, parser):
        parser.program.add_inst(Mnemonic.JUMP, parser.continue_stack[-1])


class ArrayDefinitionAction(Action):
    def do(self, parser):
        assert parser.lookahead_token.text == 'NUM'
        addr = parser.scanner.malloc(parser.lookahead_token.attribute)
        parser.program.add_inst(Mnemonic.ASSIGN, immval(addr), parser.semantic_stack[-1])


class AssignArrayAction(Action):
    def do(self, parser):
        tmp = parser.get_temp()
        parser.program.add_inst(Mnemonic.ADD, parser.semantic_stack[-3], parser.semantic_stack[-2], tmp)
        parser.program.add_inst(Mnemonic.ASSIGN, parser.semantic_stack.pop(), indval(tmp))
        parser.semantic_stack.pop()


class ArrayAccessAction(Action):
    def do(self, parser):
        tmp = parser.get_temp()
        parser.program.add_inst(Mnemonic.ADD, parser.semantic_stack.pop(), parser.semantic_stack.pop(), tmp)
        parser.semantic_stack += [indval(tmp)]


class IncreaseScopeAction(Action):
    def do(self, parser):
        parser.scope += 1


class DecreaseScopeAction(Action):
    def do(self, parser):
        parser.scope -= 1


class FunctionSaveAction(Action):
    def do(self, parser):
        activity_record_address = parser.scanner.malloc(2)
        start_pc_address = activity_record_address
        return_address_address = activity_record_address + 1
        parser.return_stack.append(return_address_address)
        # write the record address to the function symbol memory
        parser.program.add_inst(Mnemonic.ASSIGN, immval(activity_record_address), parser.semantic_stack[-1])
        # write the start address to the first word of activity record
        parser.program.add_inst(Mnemonic.ASSIGN, immval(parser.program.pc + 2), start_pc_address)
        parser.semantic_stack.append(parser.program.pc)
        parser.program.add_fake_inst()  # skip running the function on the first pass


class FunctionAction(Action):
    def do(self, parser):
        parser.program.edit_inst(parser.semantic_stack.pop(), Mnemonic.JUMP, parser.program.pc + 1)
        parser.program.add_inst(Mnemonic.JUMP, indval(parser.return_stack.pop()))


class FunctionReturnAction(Action):
    def do(self, parser):
        parser.program.add_inst(Mnemonic.JUMP, indval(parser.return_stack[-1]))


class CallMainAction(Action):
    def do(self, parser):
        main_symbol_address = parser.scanner.get_symbol_address('main')
        activity_record_address = parser.get_temp()
        return_address_address = parser.get_temp()
        parser.program.add_inst(Mnemonic.ASSIGN, main_symbol_address, activity_record_address)
        parser.program.add_inst(Mnemonic.ADD, activity_record_address, immval(1), return_address_address)
        parser.program.add_inst(Mnemonic.ASSIGN, immval(parser.program.pc + 3), indval(return_address_address))
        start_pc = parser.get_temp()
        parser.program.add_inst(Mnemonic.ASSIGN, indval(activity_record_address), start_pc)
        parser.program.add_inst(Mnemonic.JUMP, indval(start_pc))
        parser.program.add_nop()


class PullIDAction(Action):
    def do(self, parser):
        assert parser.lookahead_token.text == 'ID'
        parser.program.add_pop(parser.lookahead_token.attribute)


class CallAction(Action):
    def do(self, parser):
        function_symbol_address = parser.semantic_stack[-1]
        activity_record_address = parser.get_temp()
        return_address_address = parser.get_temp()
        parser.program.add_inst(Mnemonic.ASSIGN, function_symbol_address, activity_record_address)
        parser.program.add_inst(Mnemonic.ADD, activity_record_address, immval(1), return_address_address)
        parser.program.add_inst(Mnemonic.ASSIGN, immval(parser.program.pc + 3), indval(return_address_address))
        start_pc = parser.get_temp()
        parser.program.add_inst(Mnemonic.ASSIGN, indval(activity_record_address), start_pc)
        parser.program.add_inst(Mnemonic.JUMP, indval(start_pc))


class PushParameterAction(Action):
    def do(self, parser):
        parser.program.add_push(parser.semantic_stack.pop())


class DefinePrintAction(Action):
    def do(self, parser):

        # # FunctionSave
        activity_record_address = parser.scanner.malloc(2)
        start_pc_address = activity_record_address
        return_address_address = activity_record_address + 1
        parser.semantic_stack.append(return_address_address)
        # write the record address to the function symbol memory
        parser.program.add_inst(Mnemonic.ASSIGN, immval(activity_record_address), 0)
        # write the start address to the first word of activity record
        parser.program.add_inst(Mnemonic.ASSIGN, immval(parser.program.pc + 2), start_pc_address)
        parser.semantic_stack.append(parser.program.pc)
        parser.program.add_fake_inst()  # skip running the function on the first pass

        # # PullID
        # # Assembly
        temporary = parser.get_temp()
        parser.program.add_pop(temporary)
        parser.program.add_inst(Mnemonic.PRINT, temporary)

        # # Function
        parser.program.edit_inst(parser.semantic_stack.pop(), Mnemonic.JUMP, parser.program.pc + 1)
        parser.program.add_inst(Mnemonic.JUMP, indval(parser.semantic_stack.pop()))
