'''
Дана цілочислова прямокутна матриця.
Переставляючи рядки даної матриці, розташувати їх у відповідності з ростом характеристик.
Характеристикою рядка цілочислової матриці назвемо суму її додатних парних елементів.
'''

import random
n = int(input('n= '))
m = int(input('m= '))
a = [[random.randint(-15, 15) for j in range(m)] for i in range(n)]
b = [sum(filter(lambda el : (el > 0 and el % 2 == 0),row)) for row in a]

change = True
while change:
    change = False
    for i in range(1, len(b)):
        if b[i-1] > b[i]:
            b[i-1], b[i] = b[i], b[i-1]
            a[i - 1], a[i] = a[i], a[i - 1]
            change = True

print(*a, sep = '\n')