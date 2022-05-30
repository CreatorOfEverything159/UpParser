from lparser import LRParser


rules = [
    'E -> T+E',
    'E -> T',
    'T -> F*T',
    'T -> F',
    'F -> a'
]
enter = 'a+a'

# rules = [
#     # 'S -> aGc',
#     # 'S -> ac',
#     # 'S -> bA',
#     # 'S -> b',
#     # 'S -> $',
#     # 'G -> aGc',
#     # 'G -> ac',
#     # 'G -> bA',
#     # 'G -> b',
#     # 'A -> bA',
#     # 'A -> b'
# ]
# enter = 'abc'


if __name__ == '__main__':
    parser = LRParser(rules, enter)
    parser.run()
    print(parser.homomorphism())
