# Дана цілочислова квадратна матриця. Розмістити елементи непарних рядків у порядку зростання.

import random
n = int(input('n = '))
a = [[random.randint(0, 50) for j in range(n)] for i in range(n)]
print(*a, sep='\n')

a[1::2] = sorted(a)
print(a[1::2])
