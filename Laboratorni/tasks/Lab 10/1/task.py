'''
Об’єкт “Вектор”

поля        для зберігання координат вектора;
            для зберігання розмірності вектора;

методи      введення елементів вектора;
            виведення елементів вектора у рядку;
            визначення довжини вектора;
            нормування вектора.
'''
import random

class Vector:
    def __init__(self, coordinates=[]):
        self.coordinates = coordinates
    def len(self):
        return len(self.coordinates)
    def __str__(self):
        return 'v = {0}'.format(self.coordinates)

v = Vector([random.randint(-100, 100) for el in range(int(input('Кількість ел. у векторі: ')))])
print(v)
print('len = {0}'.format(v.len()))
print('Нормований вектор: {0}'.format(list(map(lambda i: i / (sum(map(lambda x: x**2, v)))**(1/2), v))))