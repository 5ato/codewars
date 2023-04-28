class BlockParameters:
    def __set_name__(self, owner: type, name: str):
        self.name = '__' + name

    def __get__(self, instance: 'Block', owner: type):
        return getattr(instance, self.name)

    def __set__(self, instance: 'Block', value: int):
        if value < 0:
            raise ValueError('Must be greater than 0')
        setattr(instance, self.name, value)


class Block:
    height = BlockParameters()
    width = BlockParameters()
    length = BlockParameters()

    def __init__(self, parameters: list[int]) -> None:
        self.width: int = parameters[0]
        self.length: int = parameters[1]
        self.height: int = parameters[2]
    
    def get_width(self) -> int:
        return self.width
    
    def get_length(self) -> int:
        return self.length
    
    def get_height(self) -> int:
        return self.height
    
    def get_volume(self) -> int:
        return self.width * self.length * self.height
    
    def get_surface_area(self) -> int:
        return (self.width * self.length + self.length * self.height + self.height * self.width) * 2
    


if __name__ == '__main__':
    b = Block(5, 5, 5)