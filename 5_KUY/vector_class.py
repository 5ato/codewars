class Vector:
    def __init__(self, parametrs: list[int]) -> None:
        self.parametrs: list = parametrs
        self.count = 0
        
    def __str__(self) -> str:
        return f'({",".join([str(i) for i in self.parametrs])})'
    
    def __iter__(self):
        self.count = 0
        return self
    
    def __getitem__(self, index: int):
        return self.parametrs[index]
    
    def __next__(self):
        if self.count == len(self.parametrs):
            raise StopIteration
        else:
            value = self.parametrs[self.count]
            self.count += 1
            return value
    
    def __len__(self):
        return len(self.parametrs)
    
    def verify_count_parametrs(f):
        def wrap(self, other):
            if len(self) != len(other):
                raise ValueError('Must be the same length')
            return f(self, other)
        return wrap

    @verify_count_parametrs
    def add(self, other: 'Vector') -> 'Vector':
        return Vector([self[i] + other[i] for i in range(len(self))])
    
    @verify_count_parametrs
    def subtract(self, other: 'Vector') -> 'Vector':
        return Vector([self[i] - other[i] for i in range(len(self))])
    
    @verify_count_parametrs
    def dot(self, other: 'Vector') -> int:
        return sum([self[i] * other[i] for i in range(len(self))])
    
    def norm(self) -> int:
        return sum([i ** 2 for i in self]) ** 0.5
    
    def equals(self, other: 'Vector') -> bool:
        return all([self[i] == other[i] for i in range(len(self))])


if __name__ == '__main__':
    v = Vector([1, 2, 3])
    c = Vector([1, 2, 4, 5])
    print(not c.equals(v))
    