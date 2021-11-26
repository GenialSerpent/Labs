# Дано матрицю A[m*n] та матриця В такої самої розмірності. Замінити всі нульові елементи матриці А відповідними елементами матриці В.
import random
from functools import reduce
m=int(input('m = '))
n=int(input('n = '))
a = [[random.randint(-10, 10) for e in range(n)] for f in range(m)]
b = [[random.randint(-10, 10) for x in range(n)] for y in range(m)]
print(*a, sep='\n')
print(*b, sep='\n')
'''
for i in range(len(b)):
    for j in range(len(b[i])):
        o = [b[i][j] + a[i][j] for row in a if a[i][j] == 0]
        print(o)
'''
o = filter(lambda i : i == 0, a)
s = list(reduce((lambda prevSum, row:  prevSum + sum(row)), o))
print(*s, sep='\n')