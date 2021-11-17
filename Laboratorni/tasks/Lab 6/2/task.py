'''
Задано масив B=(b[i]), i=(1, 2, ..., n) , де:

b[i]=1+1/2+...+1/i    if i%2=0
b[i]=i!/2+3           if i%2=1

Знайти добуток елементів масиву В з непарними номерами.
'''

import math
n = int(input('Кількість значень в і: '))
i = range(1, n+1)
d = 1

c = [math.factorial(b) / 2 + 3 for b in i if b % 2 == 1]
print('Масив з непарними числами: {0}'.format(c))
for x in c:
   d *= x
print('Добуток елементів масиву: {0}'.format(d))