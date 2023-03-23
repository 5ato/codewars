import collections


class UnexpectedTypeException(Exception):
    def __init__(self, *args):
        if args:
            self.message: str = args[0]

    def __str__(self):
        if self.message:
            return self.message


def expected_type(*return_types):
    """Check if decorated function returns object of return_types or raise UnexpectedTypeException.
    
    Example:
    
    @expected_type((str,))
    def return_something(input):
        # do stuff here with the input...
        return something
    
    >>> return_something('The quick brown fox jumps over the lazy dog.')
    'The quick brown fox jumps over the lazy dog.'

    >>> return_something('The quick brown fox jumps over the lazy dog.')
    'Maybe you'll output another string...'
    
    >>> return_something(None)
    UnexpectedTypeException: Was expecting instance of: str
    
    """
    def outer(func):
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            for return_type in return_types:
                if return_type == type(result) or issubclass(type(result), return_type):
                    return result
            raise UnexpectedTypeException(f'Was expecting instance of: {return_types}')
        return inner
    return outer


@expected_type(str, int, list, dict)
def do_something(a, b):
    return collections.Counter()


def main():
    print(do_something(5, 5))


if __name__ == '__main__':
    main()
