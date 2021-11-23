# Дана цілочислова прямокутна матриця. Визначити суму додатних елементів матриці з першим парним і другим непарним індексами.
import random

a = [
    [random.randint(-100, 100) for x in range(5)],
    [random.randint(-100, 100) for y in range(5)],
    [random.randint(-100, 100) for z in range(5)],
    [random.randint(-100, 100) for n in range(5)]
]

s = 0

for row in a[2::2]:
    for el in row[1::2]:
        if el > 0:
            s += el
print(*a, sep='\n')

print('Сума = {0}'.format(s))