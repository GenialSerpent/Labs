# Дано вектор xєR**n і число aєR. Знайти добуток вектора на число.
import random
m = float(input('Введіть число: '))
n = int(input('Кількість елементів у векторі: '))

x = []
y = []

for i in range(n):
    x.append(random.randint(-100, 100))
print('Вектор х = {0}'.format(x))
for a in x:
    a *= m
    y.append(a)
print('Вектор у = {0}'.format(y))