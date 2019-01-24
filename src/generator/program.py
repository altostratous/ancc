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

class Inst:
    def __init__(self, mne, *args):
        self.arr = [mne, *args]

    @staticmethod
    def fake():
        return Inst(Mnemonic.FAKE)

    def __str__(self):
        return '(' + ', '.join(self.arr) +')'

    def __repr__(self):
        return str(self)


class Program:
    def __init__(self):
        self.insts = []
        self.pc = 0

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

    def edit_inst(self, index, inst):
        assert self.insts[index][0] == Mnemonic.FAKE
        self.insts[index] = inst
