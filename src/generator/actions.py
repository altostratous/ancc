from generator.defines import Mnemonic
from generator.utils import indval, immval
from grammar.models import Literal
from core.defines import DataType, DeclarationType
from scanner.errors import SemanticError


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
        if parser.semantic_stack[-1] == 'None' or parser.semantic_stack[-3] == 'None':
            raise SemanticError('Cannot add/sub a void value', parser.scanner)
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
        if parser.semantic_stack[-1] == 'None' or parser.semantic_stack[-3] == 'None':
            raise SemanticError('Cannot compare a void value', parser.scanner)

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
        if parser.semantic_stack[-1] == 'None' or parser.semantic_stack[-2] == 'None':
            raise SemanticError('Cannot mult a void value', parser.scanner)

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
        if parser.semantic_stack[-2] == 'None':
            raise SemanticError('Cannot use a void value as if condition', parser.scanner)

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
        if parser.semantic_stack[-2] == 'None':
            raise SemanticError('Cannot use a void value as while condition', parser.scanner)

        parser.program.edit_inst(parser.semantic_stack.pop(), Mnemonic.JUMP_FALSE,
                                 parser.semantic_stack.pop(), parser.program.pc + 1)
        parser.program.add_inst(Mnemonic.JUMP, parser.semantic_stack.pop())
        parser.program.edit_inst(parser.break_stack.pop(), Mnemonic.JUMP, parser.program.pc)
        parser.continue_stack.pop()


class SwitchPushTestAction(Action):
    def do(self, parser):
        test = parser.get_temp()
        default = parser.get_temp()
        parser.program.add_inst(Mnemonic.ASSIGN, immval(1), default)
        parser.program.add_inst(Mnemonic.ASSIGN, immval(0), test)
        parser.program.add_inst(Mnemonic.JUMP, parser.program.pc + 2)
        parser.semantic_stack.append(parser.program.pc)
        parser.break_stack.append(parser.program.pc)
        parser.program.add_fake_inst()
        parser.semantic_stack.append(default)
        parser.semantic_stack.append(test)


class SwitchPopAction(Action):
    def do(self, parser):
        parser.semantic_stack.pop()
        parser.semantic_stack.pop()
        parser.semantic_stack.pop()
        parser.program.edit_inst(parser.semantic_stack.pop(), Mnemonic.JUMP, parser.program.pc)


class SwitchTestAction(Action):
    def do(self, parser):
        test = parser.semantic_stack[-2]
        default = parser.semantic_stack[-3]
        is_equal = parser.get_temp()
        parser.program.add_inst(
            Mnemonic.EQUALS, parser.semantic_stack[-1], immval(parser.lookahead_token.attribute), is_equal
        )
        parser.program.add_inst(
            Mnemonic.JUMP_FALSE, is_equal, parser.program.pc + 3
        )
        parser.program.add_inst(Mnemonic.ASSIGN, immval(1), test)
        parser.program.add_inst(Mnemonic.ASSIGN, immval(0), default)


class SwitchSaveAction(Action):
    def do(self, parser):
        parser.semantic_stack.append(parser.program.pc)
        parser.program.add_fake_inst()


class SwitchPatchJumpOnTestAction(Action):
    def do(self, parser):
        default = parser.semantic_stack[-4]
        if default == 'None':
            raise SemanticError('Cannot use a void value as switch condition', parser.scanner)

        parser.program.edit_inst(parser.semantic_stack.pop(), Mnemonic.JUMP_FALSE, default, parser.program.pc)


class SwitchPatchJumpOnNotTestAction(Action):
    def do(self, parser):
        test = parser.semantic_stack[-3]
        if test == 'None':
            raise SemanticError('Cannot use a void value as switch condition', parser.scanner)

        parser.program.edit_inst(parser.semantic_stack.pop(), Mnemonic.JUMP_FALSE, test, parser.program.pc)


class PushIDAction(Action):
    def do(self, parser):
        assert parser.lookahead_token.text == 'ID'
        parser.semantic_stack += [parser.lookahead_token.attribute]


class AssignAction(Action):
    def do(self, parser):
        if parser.scanner.get_token_by_address(parser.semantic_stack[-2]) and parser.scanner.get_token_by_address(parser.semantic_stack[-2]).declaration_type == DeclarationType.ARRAY:
            raise SemanticError('Assignment to array is not allowed', parser.scanner)
        if parser.scanner.get_token_by_address(parser.semantic_stack[-1]) and parser.scanner.get_token_by_address(parser.semantic_stack[-1]).declaration_type == DeclarationType.ARRAY:
            raise SemanticError('Assignment from array is not allowed', parser.scanner)
        parser.program.add_inst(Mnemonic.ASSIGN, parser.semantic_stack.pop(),
                                parser.semantic_stack[-1])


class PopIDAction(Action):
    def do(self, parser):
        parser.semantic_stack.pop()


class BreakAction(Action):
    def do(self, parser):
        if len(parser.break_stack) == 0:
            raise SemanticError('`break` statement has no parent `while` or `switch`', parser.scanner)
        parser.program.add_inst(Mnemonic.JUMP, parser.break_stack[-1])


class ContinueAction(Action):
    def do(self, parser):
        if len(parser.continue_stack) == 0:
            raise SemanticError('`continue` statement has no parent `while`', parser.scanner)
        parser.program.add_inst(Mnemonic.JUMP, parser.continue_stack[-1])


class ArrayDefinitionAction(Action):
    def do(self, parser):
        assert parser.lookahead_token.text == 'NUM'
        parser.scanner.get_token_by_address(parser.semantic_stack[-1]).declaration_type = DeclarationType.ARRAY
        parser.scanner.analyze_semantics()
        addr = parser.scanner.malloc(parser.lookahead_token.attribute)
        parser.program.add_inst(Mnemonic.ASSIGN, immval(addr), parser.semantic_stack[-1])


class AssignArrayAction(Action):
    def do(self, parser):
        if parser.scanner.get_token_by_address(parser.semantic_stack[-1]) and parser.scanner.get_token_by_address(parser.semantic_stack[-1]).declaration_type == DeclarationType.ARRAY:
            raise SemanticError('Assignment from array is not allowed', parser.scanner)
        tmp = parser.get_temp()
        parser.program.add_inst(Mnemonic.ADD, parser.semantic_stack[-3], parser.semantic_stack[-2], tmp)
        parser.program.add_inst(Mnemonic.ASSIGN, parser.semantic_stack.pop(), indval(tmp))
        parser.semantic_stack.pop()
        parser.semantic_stack.pop()
        parser.semantic_stack += [indval(tmp)]


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
        parser.scanner.get_token_by_address(parser.semantic_stack[-1]).declaration_type = DeclarationType.FUNCTION
        parser.function_stack += [parser.scanner.get_token_by_address(parser.semantic_stack[-1])]
        parser.scanner.analyze_semantics()
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
        if parser.function_stack[-1].has_return == False and parser.function_stack[-1].data_type != DataType.VOID:
            raise SemanticError('Missing return statement inside the function', parser.scanner)
        if len(parser.function_stack) == 1 and parser.function_stack[-1].lexeme == 'main' and parser.function_stack[-1].data_type != DataType.VOID:
            raise SemanticError('Invalid prototype for function main', parser.scanner)
        parser.function_stack.pop()


class FunctionReturnAction(Action):
    def do(self, parser):
        parser.function_stack[-1].has_return = True
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
        function_data_type = parser.scanner.get_token_by_address(function_symbol_address).data_type
        activity_record_address = parser.get_temp()
        return_address_address = parser.get_temp()
        parser.program.add_inst(Mnemonic.ASSIGN, function_symbol_address, activity_record_address)
        parser.program.add_inst(Mnemonic.ADD, activity_record_address, immval(1), return_address_address)
        parser.program.add_inst(Mnemonic.ASSIGN, immval(parser.program.pc + 3), indval(return_address_address))
        start_pc = parser.get_temp()
        parser.program.add_inst(Mnemonic.ASSIGN, indval(activity_record_address), start_pc)
        parser.program.add_inst(Mnemonic.JUMP, indval(start_pc))
        if function_data_type == DataType.INTEGER:
            return_value = parser.get_temp()
            parser.program.add_pop(return_value)
            parser.semantic_stack[-1] = return_value
        else:
            parser.semantic_stack[-1] = 'None'
        if parser.argument_stack[-1]:
            raise SemanticError('Too few arguments passed', parser.scanner)
        parser.argument_stack.pop()


class CallBeforeAction(Action):
    def do(self, parser):
        function_symbol_address = parser.semantic_stack[-1]
        prototype = parser.scanner.get_token_by_address(function_symbol_address).prototype
        parser.argument_stack += [prototype[:]]


class PushParameterAction(Action):
    def do(self, parser):
        top_of_stack = parser.semantic_stack.pop()
        if top_of_stack == 'None':
            raise SemanticError('Cannot pass a void argument to a function', parser.scanner)
        if not parser.argument_stack[-1]:
            raise SemanticError('Too many arguments passed', parser.scanner)
        if isinstance(top_of_stack, str) and top_of_stack[0] == '#':
            if parser.argument_stack[-1][0].declaration_type == DeclarationType.ARRAY:
                print(parser.argument_stack[-1])
                raise SemanticError('Cannot convert an integer literal to an array', parser.scanner)

        if isinstance(top_of_stack, int) and parser.scanner.get_token_by_address(top_of_stack) and parser.scanner.get_token_by_address(top_of_stack).declaration_type == DeclarationType.ARRAY:
            if parser.argument_stack[-1][0].declaration_type == DeclarationType.VARIABLE:
                raise SemanticError('Cannot convert an array to an integer type', parser.scanner)

        if parser.scanner.get_token_by_address(top_of_stack) and parser.scanner.get_token_by_address(top_of_stack).declaration_type == DeclarationType.FUNCTION:
            raise SemanticError('Cannot pass a function to a function', parser.scanner)

        parser.argument_stack[-1] = parser.argument_stack[-1][1:]
        parser.program.add_push(top_of_stack)


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


class PushReturnValueAction(Action):
    def do(self, parser):
        if parser.function_stack[-1].data_type == DataType.VOID:
            raise SemanticError('Invalid return value for a void function', parser.scanner)
        parser.program.add_push(parser.semantic_stack.pop())

class NoReturnAction(Action):
    def do(self, parser):
        if parser.function_stack[-1].data_type != DataType.VOID:
            raise SemanticError('Invalid return value for a non-void function', parser.scanner)



class VarDefinitionAction(Action):
    def do(self, parser):
        parser.scanner.get_token_by_address(parser.semantic_stack[-1]).declaration_type = DeclarationType.VARIABLE
        parser.scanner.analyze_semantics()


class NewParamAction(Action):
    def do(self, parser):
        token = parser.lookahead_token
        if token.data_type == DataType.VOID:
            raise SemanticError("Cannot declare a variable with void type", parser.scanner)
        token.declaration_type = DeclarationType.VARIABLE
        if len(parser.function_stack) == 1 and parser.function_stack[-1].lexeme == 'main':
            raise SemanticError('Invalid prototype for function main', parser.scanner)
        parser.function_stack[-1].prototype.append(token)


class ArrayParamAction(Action):
    def do(self, parser):
        parser.function_stack[-1].prototype[-1].declaration_type = DeclarationType.ARRAY