class State:

    COUNT = 1

    def __init__(self, is_success=False):
        self.id = State.COUNT
        State.COUNT += 1
        self.actions = []
        self.nexts = []
        self.is_success = is_success

    def __str__(self):
        return str(self.id) + (' (success)' if self.is_success else '')

    def __repr__(self):
        return str(self)

    def full_repr(self):
        return str(self) + (' to -> ' + str(self.nexts) if not self.is_success else '')