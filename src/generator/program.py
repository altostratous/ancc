def immval(x):
    return '#' + str(x)


def indval(x):
    return '@' + str(x)


class Mnemonic:
    ASSIGN = 'ASSIGN'
    ADD = 'ADD'
    SUBTRACT = 'SUB'
    MULTIPLY = 'MULT'
    NOT = 'NOT'
    AND = 'AND'
    EQUALS = 'EQ'
    LESS_THAN = 'LT'
    JUMP_FALSE = 'JPF'
    JUMP = 'JP'
    PRINT = 'PRINT'
    FAKE = 'FAKE'
    PUSH = 'PUSH'
    POP = 'POP'
    NOP = 'NOP'


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
    def __init__(self, stack):
        self.insts = []
        self.pc = 0
        self.sp = stack

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
        self.add_inst(Mnemonic.ASSIGN, arg, self.sp)
        self.add_inst(Mnemonic.ADD, self.sp, immval(1), self.sp)

    def add_pop(self, arg):
        self.add_inst(Mnemonic.ASSIGN, self.sp, arg)
        self.add_inst(Mnemonic.SUBTRACT, self.sp, immval(1), self.sp)

    def edit_inst(self, index, *args):
        assert self.insts[index].arr[0] == Mnemonic.FAKE
        self.insts[index] = Inst(*args)
