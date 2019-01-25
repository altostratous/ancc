class ANCCError(Exception):
    def __init__(self, scanner, *args: object) -> None:
        super().__init__(*args)
        self.line, self.column = scanner.line_and_column()
        self.summary = scanner.summary()

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "Error: {}:{}: \n{}\n".format(self.line, self.column, self.summary)


class ParseError(ANCCError):

    def __init__(self, lookahead, non_terminal, *args):
        super().__init__(*args)
        self.lookahead = lookahead
        self.non_terminal = non_terminal

    def __str__(self):
        return "Unexpected {} in {}".format(
            self.lookahead, self.non_terminal
        )

    def __repr__(self):
        return str(self)