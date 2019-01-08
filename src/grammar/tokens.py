class Token(object):

    def __init__(self, text, attribute, literal):
        super(Token, self).__init__()
        self.text = text
        self.attribute = attribute
        self.literal = literal

    def __eq__(self, o) -> bool:
        if o is None:
            return False
        return o.text == self.text and o.attribute == self.attribute

    def __str__(self) -> str:
        return 'Token(`{}`, {})'.format(self.text, self.attribute)

    def __repr__(self) -> str:
        return str(self)
