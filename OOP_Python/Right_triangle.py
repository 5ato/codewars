class RightTriangle:

    __do = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
    }

    def __init__(self, hypotenuse: int, cathetus1: int, cathetus2: int):
        self.cathetus1: int = cathetus1
        self.cathetus2: int = cathetus2
        self.hypotenuse: int = hypotenuse

    def up_side(self, side: str, percent: int, do='+'):
        if do.strip() not in ('+', '-'):
            raise ValueError('Only + or -')
        if side.lower().strip() not in ('cathetus1', 'cathetus2', 'hypotenuse'):
            raise AttributeError('No such side')

        percent /= 100

        if side.lower().strip() == 'cathetus1':
            self.cathetus1 = RightTriangle.__do[do](self.cathetus1, self.cathetus1 * percent)
        elif side.lower().strip() == 'cathetus2':
            self.cathetus2 = RightTriangle.__do[do](self.cathetus2, self.cathetus2 * percent)
        else:
            self.hypotenuse = RightTriangle.__do[do](self.hypotenuse, self.hypotenuse * percent)
    
    def radius_circumscribed_circle(self):
        return 0.5 * self.hypotenuse

    def Perimeter(self):
        return self.cathetus1 + self.cathetus2 + self.hypotenuse
