# Дано n дійсних чисел: x1, x2, ..., xn. Знайти середнє геометричне значення цих чисел.

import random
n = int(input('Кількість чисел: '))
a = []
m = 1

for i in range(1, n+1):
    a.append(float(random.randint(1, 100)))
for x in a:
    m *= x
res = m**(1/n)

print('середнє геометричне = {0:.4}'.format(res))



