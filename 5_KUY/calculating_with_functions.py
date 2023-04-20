"""
https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39
"""


operations = {
    '-': lambda x, y: x - y,
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x // y,
}


zero: int = lambda arg = None: 0 if arg is None else operations[arg[0]](0, arg[1])
one: int = lambda arg = None: 1 if arg is None else operations[arg[0]](1, arg[1])
two: int = lambda arg = None: 2 if arg is None else operations[arg[0]](2, arg[1])
three: int = lambda arg = None: 3 if arg is None else operations[arg[0]](3, arg[1])
four: int = lambda arg = None: 4 if arg is None else operations[arg[0]](4, arg[1])
five: int = lambda arg = None: 5 if arg is None else operations[arg[0]](5, arg[1])
six: int = lambda arg = None: 6 if arg is None else operations[arg[0]](6, arg[1])
seven: int = lambda arg = None: 7 if arg is None else operations[arg[0]](7, arg[1])
eight: int = lambda arg = None: 8 if arg is None else operations[arg[0]](8, arg[1])
nine: int = lambda arg = None: 9 if arg is None else operations[arg[0]](9, arg[1])


plus: list = lambda arg: ['+', arg]
minus: list = lambda arg: ['-', arg]
times: list = lambda arg: ['*', arg]
divided_by: list = lambda arg: ['/', arg]
