import os
from os import path


class DataType(object):
    INTEGER = 'int'
    VOID = 'void'


class DeclarationType(object):
    ARRAY = 'array'
    FUNCTION = 'function'
    VARIABLE = 'variable'


RESERVED_WORDS = ['int', 'void', 'continue', 'break', 'if', 'else', 'while', 'return', 'switch', 'case', 'default']
SINGLE_CHARACTERS = [';', ',', '[', ']', '{', '}', '(', ')', ':', '*']
BASE_DIR = path.dirname(os.path.dirname(os.path.dirname(__file__)))