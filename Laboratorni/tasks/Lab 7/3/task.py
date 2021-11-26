#Дано матрицю A(m*n) та вектор x(n). Перевірити, чи виконується рівність Ax=b
import random

m = int(input('m= '))
n = int(input('n= '))
a = [[random.randint(-20, 20)for q in range(n)]for r in range(m)]
b = [random.randint(-20, 20)for el in range(n)]
x = [random.randint(-20, 20)for y in range(n)]

is_x_solution = True
for i in range(len(a)):
    s = 0
    for j in range(len(a[i])):
        s += a[i][j] * x[j]
    if s != b[i]:
        is_x_solution = False
        break

if is_x_solution:
    print('Ax=b')
else:
    print('Ax!=b')