from generator.program import Program
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


class ParseError(Exception):

    def __init__(self, lookahead, non_terminal, *args):
        super().__init__(*args)
        self.lookahead = lookahead
        self.non_terminal = non_terminal

    def __str__(self):
        return "Unexpected {} in {}.".format(
            self.lookahead, self.non_terminal
        )

    def __repr__(self):
        return str(self)


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
        self.tree = (start_state.non_terminal.text, [])
        self.tree_stack = [self.tree]
        self.semantic_stack = []
        self.program = Program()
        self.errors = []

    @property
    def lookahead_literal(self):
        if self.lookahead_token is None:
            return None
        return self.lookahead_token.literal

    @property
    def lookahead_token(self):
        if self._lookahead is None:
            next_token = self.scanner.get_next_token()
            if next_token:
                self._lookahead = next_token
        return self._lookahead

    def match(self, s):
        if self.lookahead_literal != s:
            return False
        self.tree_stack[-1][1].append(self.lookahead_literal.text)
        self._lookahead = None
        return True

    def find_next_state(self, current_state):
        if current_state.is_success:
            return None, None, None
        for literal, next_state in current_state.nexts:
            # ε transition
            if not literal and self.lookahead_literal in self.follow[current_state.non_terminal]:
                assert next_state.is_success
                return next_state, None, None
            elif literal.is_action:
                literal.do(self)
                return next_state, None, None
            # an ε potent rule
            elif not literal.is_terminal and () in self.first[literal] and self.lookahead_literal in self.follow[literal]:
                return next_state, literal, None
            elif literal.is_terminal:
                if self.match(literal):
                    return next_state, None, None
            elif self.lookahead_literal in self.first[literal]:
                return next_state, literal, None
        print(self.stack)
        return None, None, ParseError(self.lookahead_literal, current_state.non_terminal)

    def parse(self):
        while self.stack and self.lookahead_literal:
            next_state, new_flow, error = self.find_next_state(self.stack[-1])
            if error:
                self.errors.append(error)
                current_non_terminal = self.stack[-1].non_terminal
                while self.lookahead_literal not in self.follow[current_non_terminal]:
                    self._lookahead = None
                while not self.stack[-1].is_success:
                    self.stack[-1] = self.stack[-1].nexts[0][1]
                continue
            if next_state is None:
                if len(self.stack) > 1:
                    self.stack[-2] = dict(self.stack[-2].nexts)[self.stack[-1].non_terminal]
                self.parsed(self.stack.pop())
            else:
                if new_flow:
                    state_to_push = self.state_machines[new_flow]
                    self.stack.append(state_to_push)
                    self.entered(state_to_push)
                else:
                    self.stack[-1] = next_state
        return self.errors

    # noinspection PyUnusedLocal
    def parsed(self, state):
        if len(self.stack) > 0:
            self.tree_stack.pop()

    def entered(self, state):
        opening = (state.non_terminal.text, [])
        self.tree_stack[-1][1].append(opening)
        self.tree_stack.append(opening)
