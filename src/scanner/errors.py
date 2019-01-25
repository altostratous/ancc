from parser.errors import ANCCError


class SemanticError(ANCCError):
    def __init__(self, text, *args: object) -> None:
        super().__init__(*args)
        self.text = text

    def __repr__(self):
        return str(self)

    def __str__(self):
        return super().__str__() + "Semantic Error"


class DuplicateDeclaration(SemanticError):

    def __str__(self):
        return super(DuplicateDeclaration, self).__str__() + ": Duplicate declaration of ID {}".format(self.text)


class UndefinedIDError(SemanticError):

    def __str__(self):
        return super(UndefinedIDError, self).__str__() + ": Undefined ID {}".format(self.text)