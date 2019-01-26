class ANCCError(Exception):
    def __init__(self, scanner, *args: object) -> None:
        super().__init__(*args)
        self.line, self.column = scanner.line_and_column()
        self.summary = scanner.summary()

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "Error at line {} near `{}`".format(self.line, self.summary)


class ParseError(ANCCError):

    def __init__(self, lookahead_literal, non_terminal, *args):
        super().__init__(*args)
        self.lookahead_literal = lookahead_literal
        self.non_terminal = non_terminal

    def __str__(self):
        return super().__str__() + ", unexpected {} in {}".format(
            self.lookahead_literal.verbose_name, self.non_terminal.verbose_name
        )
