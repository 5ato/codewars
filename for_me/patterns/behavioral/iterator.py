from typing import Iterable, Iterator
from datetime import datetime, timedelta


# Основная мысль заключается в том, что создаётся отдельный класс для итерируемого класса
# Чтобы создать возможность итерации
# Ниже предоставлен пример работы с датой паттерна Iterator 


class DateIterator(Iterator):
    type_time = {
        'day': lambda x, y: x + timedelta(days=y),
        'week': lambda x, y: x + timedelta(weeks=y),
        'month': lambda x, y: x + timedelta(days=y*30),
        'year': lambda x, y: x + timedelta(days=y*365),
    }

    def __init__(self, start: datetime, end: datetime, type_iterator: str, range_step) -> None:
        if type_iterator not in self.type_time:
            raise ValueError('Not')
        self.start = start
        self.end = end
        self.type_iterator = type_iterator
        self.range_step = range_step

    def __next__(self):
        self.start = self.type_time[self.type_iterator](self.start, self.range_step)
        if self.start >= self.end:
            raise StopIteration
        return self.start


class PeriodDate(Iterable):
    def __init__(self, start_time: str, end_time: str):
        start_time = start_time.split('-')
        end_time = end_time.split('-')
        self.start_time: datetime = datetime(int(start_time[0]), int(start_time[1]), int(start_time[2]))
        self.end_time: datetime = datetime(int(end_time[0]), int(end_time[1]), int(end_time[2]))

    def __iter__(self) -> DateIterator:
        return DateIterator(self.start_time, self.end_time, 'week', 7)


if __name__ == '__main__':
    p = PeriodDate('2000-1-1', '2012-1-1')
    count = 0
    for i in p:
        print(i)
        count += 1
    print(count)
