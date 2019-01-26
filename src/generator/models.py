from generator.defines import Mnemonic
from generator.utils import indval, immval


class Inst:
    def __init__(self, mne, *args):
        if mne == Mnemonic.NOP:
            self.arr = [Mnemonic.ASSIGN, '0', '0']
            return
        assert Mnemonic != Mnemonic.POP
        assert Mnemonic != Mnemonic.PUSH
        self.arr = [mne, *map(str, args)]

    @staticmethod
    def fake():
        return Inst(Mnemonic.FAKE)

    @staticmethod
    def nop():
        return Inst(Mnemonic.NOP)

    def __str__(self):
        return '(' + ', '.join(self.arr) + ')'

    def __repr__(self):
        return str(self)


class Program:
    def __init__(self, stack_address):
        self.insts = []
        self.pc = 0
        self.sp = stack_address
        self.add_inst(Mnemonic.ASSIGN, immval(stack_address + 1), self.sp)

    def __str__(self):
        s = ''
        for i, inst in enumerate(self.insts):
            s += str(i) + '\t' + str(inst) + '\n'
        return s

    def add_inst(self, *args):
        self.insts += [Inst(*args)]
        self.pc += 1

    def add_fake_inst(self):
        self.insts += [Inst.fake()]
        self.pc += 1

    def add_word(self):
        self.add_nop()

    def add_nop(self):
        self.insts += [Inst.nop()]
        self.pc += 1

    def add_push(self, arg):
        self.add_inst(Mnemonic.ASSIGN, arg, indval(self.sp))
        self.add_inst(Mnemonic.ADD, self.sp, immval(1), self.sp)

    def add_pop(self, arg):
        self.add_inst(Mnemonic.SUBTRACT, self.sp, immval(1), self.sp)
        self.add_inst(Mnemonic.ASSIGN, indval(self.sp), arg)

    def edit_inst(self, index, *args):
        assert self.insts[index].arr[0] == Mnemonic.FAKE
        self.insts[index] = Inst(*args)
