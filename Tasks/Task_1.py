# Python program showing
# abstract base class work


"""
Cоздать класс Triad (тройка чисел); определить метод сравнения
триад (см. задание 2).Определить производный класс Date с полями:
год, месяц и день. Определить полный набор методов сравнения дат.
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

    @abstractmethod
    def compare(self, other):
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

    def compare(self, other):
        if self.a == other.a and self.b == other.b and self.c == other.c:
            return "Даты равны"
        else:
            return "Даты не равны"

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.c == other.c

    def __gt__(self, other):
        return (self.c, self.b, self.a) > (other.c, other.b, other.a)

    def __lt__(self, other):
        return (self.c, self.b, self.a) < (other.c, other.b, other.a)

    def __ge__(self, other):
        return (self.c, self.b, self.a) >= (other.c, other.b, other.a)

    def __le__(self, other):
        return (self.c, self.b, self.a) <= (other.c, other.b, other.a)

    def __ne__(self, other):
        return not self.__eq__(other)


if __name__ == '__main__':
    date1 = Date(17, 3, 2001)

    date1.display()
    date1.increase()
    date1.display()

    date2 = Date(17, 3, 2001)
    print(date1.compare(Date(17, 3, 2001)))

    print(date1 == date2)
    print(date1 > date2)
    print(date1 < date2)
    print(date1 >= date2)
    print(date1 <= date2)
    print(date1 != date2)
