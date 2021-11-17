# Дано дійсне число a і натуральне число n. Обчислити ln|a**n|+ln|a**(n-1)|+...+ln|a|.

import math
a = float(input('Дійсне число: '))
n = int(input('Натуральне число: '))
s = 0

while n >= 1:
    s += math.log(math.fabs(a**n), 10)
    n -= 1
print('Сума = {0:.2}'.format(s))
