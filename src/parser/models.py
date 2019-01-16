from grammar.utils import compute_non_terminals_firsts, compute_non_terminals_follows


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
        return str(self.id) + ' ({})'.format(self.non_terminal.text) + (' (success)' if self.is_success else '')

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
        self.first = compute_non_terminals_firsts(non_terminals)
        self.follow = compute_non_terminals_follows(non_terminals, self.first)

    @property
    def lookahead(self):
        if self._lookahead is None:
            self._lookahead = self.scanner.get_next_token().literal
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
            # ε transition
            if not literal and self.lookahead in self.follow[current_state.non_terminal]:
                assert next_state.is_success
                return next_state, None
            # an ε potent rule
            elif not literal.is_terminal and () in self.first[literal] and self.lookahead in self.follow[literal]:
                return next_state, literal
            elif literal.is_terminal:
                if self.match(literal):
                    return next_state, None
            elif self.lookahead in self.first[literal]:
                return next_state, literal

    def parse(self):
        while self.stack:
            next_state, new_flow = self.find_next_state(self.stack[-1])
            if next_state is None:
                if len(self.stack) > 1:
                    self.stack[-2] = dict(self.stack[-2].nexts)[self.stack[-1].non_terminal]
                self.parsed(self.stack.pop())
            else:
                if new_flow:
                    self.stack.append(self.state_machines[new_flow])
                else:
                    self.stack[-1] = next_state

    def parsed(self, param):
        pass
