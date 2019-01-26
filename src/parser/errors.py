from core.errors import ANCCError


class ParseError(ANCCError):

    def __init__(self, lookahead_literal, non_terminal, *args):
        super().__init__(*args)
        self.lookahead_literal = lookahead_literal
        self.non_terminal = non_terminal

    def __str__(self):
        return super().__str__() + ", unexpected {} in {}".format(
            self.lookahead_literal.verbose_name, self.non_terminal.verbose_name
        )
