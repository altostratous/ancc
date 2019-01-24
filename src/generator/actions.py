from generator.program import Mnemonic, immval
from grammar.models import Literal


class Action(Literal):
    @property
    def is_action(self):
        return True


class PrintAction(Action):
    def do(self, parser):
        parser.program.add_inst(Mnemonic.PRINT, immval(344))

