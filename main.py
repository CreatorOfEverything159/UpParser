from algorithm import Parser
from rule import Rule

rules = [
    Rule('E -> E+T'),
    Rule('E -> T'),
    Rule('T -> T*F'),
    Rule('T -> F'),
    Rule('F -> a')
]
enter = 'a*a'

if __name__ == '__main__':
    parser = Parser(rules, enter)
    parser.run()
