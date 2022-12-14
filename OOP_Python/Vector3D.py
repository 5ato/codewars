from math import sqrt


class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.length = self.norm()

    def __str__(self):
        return f'{self.x}, {self.y}, {self.z}'

    def __add__(self, other: 'Vector3D'):
        if not isinstance(other, Vector3D):
            raise TypeError('Должен быть экземпляр класса Вектор')

        return self.x + other.x, self.y + other.y, self.z + other.z

    def __sub__(self, other: 'Vector3D'):
        if not isinstance(other, Vector3D):
            raise TypeError('Должен быть экземпляр класса Вектор')

        return self.x - other.x, self.y - other.y, self.z - other.z
    
    def __mul__(self, other: 'Vector3D'):
        if not isinstance(other, Vector3D):
            raise TypeError('Должен быть экземпляр класса Вектор')

        return self.x * other.x, self.y * other.y, self.z * other.z

    def __truediv__(self, other: 'Vector3D'):
        if not isinstance(other, Vector3D):
            raise TypeError('Должен быть экземпляр класса Вектор')
        if 0 in (other.x, other.y, other.z):
            raise TypeError('На 0 делить нельзя')

        return self.x / other.x, self.y / other.y, self.z / other.z

    def norm(self):
        return abs(sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2))
