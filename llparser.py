from lparser import LLParser


rules = [
    'E -> E+T',
    'E -> T',
    'T -> T*F',
    'T -> F',
    'F -> a'
]
enter = 'a*a'


if __name__ == '__main__':
    parser = LLParser(rules, enter)
    parser.run()
