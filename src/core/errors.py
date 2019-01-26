class ANCCError(Exception):
    def __init__(self, scanner, *args: object) -> None:
        super().__init__(*args)
        self.line, self.column = scanner.line_and_column()
        self.summary = scanner.summary()

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "Error at line {} near `{}`".format(self.line, self.summary)