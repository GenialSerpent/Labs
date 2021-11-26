#Дана цілочислова прямокутна матриця. Визначити кількість стовпців, які не містять жодного нульового елемента.
import random

n = int(input('n= '))
m = int(input('m= '))
a = [[random.randint(-5, 5) for x in range(m)] for y in range(n)]

s = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[j] != 0:
            s += 1
print(s)