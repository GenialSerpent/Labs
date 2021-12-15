'''
Створити клас TDate для роботи із датами у форматі “день.місяць.рік”.
Дата представляється структурою із трьома полями.
Реалізувати методи збільшення/зменшення дати на певну кількість днів, місяців чи років.
Введення та виведення дати реалізувати за допомогою методу  ToString.
'''

class TDate:
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year
    def set_month(self, value):
        if 0 < value <= 12:
            self.month = value
        else:
            raise Exception('Year have only 12 months')
    def set_day(self, value):
        if 0 < value <= 31 and self.month == range(1, 8, 2) or self.month == range(8, 13, 2):
            self.day = value
        elif self.month == 2 and 0 < value <= 28:
            self.day = value
        elif 0 < value <= 30 and self.month == range(4, 7, 2) or self.month == range(9, 12, 2):
            self.day = value
        else:
            raise Exception('This month don\'t have {0} days'.format(value))

    def set_year(self, value):
        if 1960 <= value <= 2021:
            self.year = value
        else:
            raise Exception()
    def __add__(self, other):
        return TDate(self.day + other, self.month + other, self.year + other)
    def __sub__(self, other):
        return TDate(self.day - other, self.month - other, self.year - other)
    def __str__(self, day=1, month=1, year=1980):
        return '{0}. {1}. {2}p.'.format(self.day, self.month, self.year)