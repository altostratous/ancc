class Token(object):

    def __init__(self, text, attribute):
        super(Token, self).__init__()
        self.text = text
        self.attribute = attribute

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Token) and o.text == self.text and o.attribute == self.attribute

    def __str__(self) -> str:
        return 'Token(`{}`, {})'.format(self.text, self.attribute)

    def __repr__(self) -> str:
        return str(self)
