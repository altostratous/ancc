from grammar.utils import compute_first, compute_follow


class State:

    COUNT = 1

    def __init__(self, non_terminal, is_success=False):
        self.id = State.COUNT
        State.COUNT += 1
        self.actions = []
        self.nexts = []
        self.non_terminal = non_terminal
        self.is_success = is_success

    def __str__(self):
        return str(self.id) + (' (success)' if self.is_success else '')

    def __repr__(self):
        return str(self)

    def full_repr(self):
        return str(self) + (' to -> ' + str(self.nexts) if not self.is_success else '')


class Parser:
    def __init__(self, state_machines, start_state, scanner):
        self.state_machines = state_machines
        self.start_state = start_state
        self.scanner = scanner
        self._lookahead = None
        self.stack = [start_state]
        non_terminals = list(state_machines.keys())
        self.first = compute_first(non_terminals)
        self.follow = compute_follow(non_terminals, self.first)

    @property
    def lookahead(self):
        if self._lookahead is None:
            self._lookahead = self.scanner.get_next_token()
        return self._lookahead

    def match(self, s):
        if self.lookahead != s:
            return False
        self._lookahead = None
        return True

    def find_next_state(self, current_state):
        if current_state.is_success:
            return None, None
        for literal, next_state in current_state.nexts:
            if not literal:  # ε transition
                if self.lookahead in self.follow[current_state.non_terminal]:
                    assert next_state.is_success
                    return next_state, None
            elif literal.is_terminal:
                if self.match(literal.text):
                    return next_state, None
            elif self.lookahead in self.first[literal]:
                return next_state, literal

    def parse(self):
        while self.stack:
            next_state, new_flow = self.find_next_state(self.stack[-1])
            if next_state is None:
                self.stack.pop()
            else:
                self.stack[-1] = next_state
                if new_flow:
                    self.stack.append(self.state_machines[new_flow])
