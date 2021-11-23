# Дано матрицю A[m*n] та матриця В такої самої розмірності. Замінити всі нульові елементи матриці А відповідними елементами матриці В.
import random
from functools import reduce
n=int(input('n = '))
a = [
    [random.randint(-10, 10) for x in range(n)],
    [random.randint(-10, 10) for y in range(n)],
    [random.randint(-10, 10) for z in range(n)]
     ]

b = [
    [random.randint(-10, 10) for o in range(n)],
    [random.randint(-10, 10) for p in range(n)],
    [random.randint(-10, 10) for q in range(n)]
     ]

for row in b:
    for el in row:
        e=filter(lambda d : d == 0, a)
        reduce(lambda prevSum, el: prevSum + el, if prevSum == 0, a)