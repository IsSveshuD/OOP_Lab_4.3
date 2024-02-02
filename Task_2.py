# Python program showing
# abstract base class work

"""
Создать абстрактный базовый класс Triad с виртуальными методами
увеличения на 1. Создать производные классы Date (дата) и
Time (время).
"""

from abc import ABC, abstractmethod


class Triad(ABC):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @abstractmethod
    def increase(self):
        pass

    @abstractmethod
    def display(self):
        pass


class Date(Triad):
    def __init__(self, day, month, year):
        super().__init__(day, month, year)

    def increase(self):
        self.a += 1
        self.b += 1
        self.c += 1

    def display(self):
        print(f"Дата: {self.a}/{self.b}/{self.c}")


class Time(Triad):
    def __init__(self, hour, minute, second):
        super().__init__(hour, minute, second)

    def increase(self):
        self.a += 1
        self.b += 1
        self.c += 1

    def display(self):
        print(f"Время: {self.a}:{self.b}:{self.c}")


if __name__ == '__main__':
    date = Date(17, 3, 2001)
    time = Time(12, 30, 45)

    date.display()
    date.increase()
    date.display()

    time.display()
    time.increase()
    time.display()
