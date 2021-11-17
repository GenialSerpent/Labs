# Впорядкувати елементи масиву за зростанням.

import random
x = []
for i in range(7):
    x.append(random.randint(0, 100))
print('Елементи масиву: {0}'.format(x))
y = sorted(x)
print('Впорядковані ел. м. за зростанням: {0}'.format(y))
