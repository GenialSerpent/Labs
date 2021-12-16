# Реалізувати завдання попередньої лабораторної роботи з використанням властивостей для доступу до полів.

class TRectangle:
    def __init__(self, a=1, b=1):
        if a >= 1:
            self.a = a
        elif b >= 1:
            self.b = b
        else:
            raise Exception('Can\'t be less than 1')
    def input(self):
        self.a = int(input('I сторона = '))
        self.b = int(input('II сторона = '))
    def get_s(self):
        return self.a * self.b
    def get_p(self):
        return 2 * (self.a + self.b)
    def __eq__(self, r2):
        return TRectangle == r2(self.a, self.b)
    def __lt__(self, r2):
        return TRectangle < r2(self.a, self.b)
    def __le__(self, r2):
        return TRectangle <= r2(self.a, self.b)
    def __ne__(self, r2):
        return TRectangle != r2(self.a, self.b)
    def __gt__(self, r2):
        return TRectangle > r2(self.a, self.b)
    def __ge__(self, r2):
        return TRectangle >= r2(self.a, self.b)
    def __add__(self, other):
        return TRectangle(self.a + other, self.b + other)
    def __sub__(self, other):
        return TRectangle(self.a - other, self.b - other)
    def __mul__(self, x):
        return TRectangle(self.a*x, self.b*x)