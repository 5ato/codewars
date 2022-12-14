class Student:

    letter_small_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    letter_upper_ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    all_letter = letter_small_ru + letter_upper_ru + '- '

    def __init__(self, FIO: str, group_number: int, progress: list = []):
        self.FIO: str = Student.clean_FIO(FIO)
        self.group_number: int = group_number
        self.progress: list = progress

    def __str__(self):
        return f'Студент: {self.FIO}; Номер группы: {self.group_number}; Прогресс: {" ".join(list(map(str, self.progress)))}'

    @classmethod
    def clean_FIO(cls, FIO: str) -> str:
        if not isinstance(FIO, str):
            raise TypeError('ФИО должно быть строкой')
        
        if len(FIO.split()) < 3:
            raise TypeError('Некорректное содержание')
        
        for s in FIO:
            if s.isdigit() or s not in cls.all_letter:
                raise TypeError('Недопустимые символы в ФИО')
        return FIO


class Data:
    def __init__(self, data: list = []):
        self.data: list = data

    def __getitem__(self, index):
        return self.data[index]


class Pupil:
    def __init__(self):
        self.knowledge: list = []

    def study(self, info: Data):
        self.knowledge.append(info)


class Teacher:
    def __init__(self):
        self.work: int = 0

    def teach(self, info: str, pupils: list[Pupil]):
        for i in pupils:
            i.study(info)
            self.work = 1



def main():
    s = Student('Абоба боба Бобович', 2, [2, 2, 2, 2, 1, 0, 1, 2])
    print(s)


if __name__ == '__main__':
    main()
