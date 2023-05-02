"""
https://www.codewars.com/kata/5dc424122c135e001499d0e5
"""


class MetaSpecification(type):
    def __and__(self, other):
        return MetaSpecification('AndSpecification', (), {'__new__': lambda _, arg: self(arg) and other(arg)})
    
    def __or__(self, other):
        return MetaSpecification('OrSpecification', (), {'__new__': lambda _, arg: self(arg) or other(arg)})
    
    def __and__(self):
        return MetaSpecification('NotSpecification', (), {'__new__': lambda _, arg: self(arg)})
    

class Specification(metaclass=MetaSpecification):
    pass
