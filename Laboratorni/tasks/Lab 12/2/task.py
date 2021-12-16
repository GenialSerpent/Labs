'''
Створити клас TDate для роботи із датами у форматі “день.місяць.рік”.
Дата представляється структурою із трьома полями.
Реалізувати методи збільшення/зменшення дати на певну кількість днів, місяців чи років.
Введення та виведення дати реалізувати за допомогою методу  ToString.
'''

class TDate:
    def __init__(self, day=1, month=1, year=2000):
        if 1960 <= year <= 2021:
            self.year = year
        else:
            raise Exception('This year is not satisfy')

        if 0 < month <= 12:
            self.month = month
        else:
            raise Exception('Year have only 12 months')

        if 0 < day <= 31 and self.month == 1 or self.month == 3 or self.month == 5 or self.month == 7 or self.month == 8 or self.month == 10 or self.month == 12:
            self.day = day
        elif 0 < day <= 30 and self.month == 4 or self.month == 6 or self.month == 9 or self.month == 11:
            self.day = day
        elif self.month == 2 and 0 < day <= 28:
            self.day = day
        else:
            raise Exception('This month don\'t have {0} days'.format(day))
    def get_day(self):
        return self.day
    def get_month(self):
        return self.month
    def get_year(self):
        return self.year
    def __add__(self, other):
        if TDate.get_day(self):
            return TDate(self.day + other, self.month, self.year)
        elif TDate.get_month(self):
            return TDate(self.day, self.month + other, self.year)
        elif TDate.get_year(self):
            return TDate(self.day, self.month, self.year + other)
        else:
            raise Exception('Wrong command')
    def __sub__(self, other):
        if TDate.get_day(self):
            return TDate.get_day(self.day - other)
        elif TDate.get_month(self):
            return TDate.get_month(self.month - other)
        elif TDate.get_year(self):
            return TDate.get_year(self.year - other)
        else:
            raise Exception('Wrong command')
    def to_string(self):
        self.day = int(input('День: '))
        self.month = int(input('Місяць'))
        self.year = int(input('Рік: '))
    def __str__(self):
        return '{0}. {1}. {2}p.'.format(self.day, self.month, self.year)

date = TDate(23, 2, 2020)
date_2 = date.get_year() + 5
print(date)
print(date_2)