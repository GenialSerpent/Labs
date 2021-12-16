'''
Клас “Прямокутник ” – TRectangle
поля
для зберігання довжин сторін;
методи
конструктор без параметрів, конструктор з параметрами, конструктор копіювання;
введення/виведення даних;
визначення площі;
визначення периметру;
порівняння з іншим прямокутником;
перевантаження операторів + (додавання відповідних сторін), – (віднімання довжин відповідних сторін), * (множення сторін на деяке число).
'''

class TRectangle:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
    def input(self):
        self.a = int(input('I сторона = '))
        self.b = int(input('II сторона = '))
    def get_s(self):
        return self.a * self.b
    def get_p(self):
        return 2 * (self.a + self.b)
    def __eq__(self, r2):
        return TRectangle < r2
    def __add__(self, other):
        return TRectangle(self.a + other, self.b + other)
    def __sub__(self, other):
        return TRectangle(self.a - other, self.b - other)
    def __mul__(self, x):
        return TRectangle(self.a*x, self.b*x)
