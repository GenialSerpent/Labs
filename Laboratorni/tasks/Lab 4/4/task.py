'''
  {ln|x|-n   x<n
y={ln|x|=n   x=n
  {cos(n*x)  x>n
'''

import math

n = float(input('число n: '))
x = float(input('число x: '))

a = math.fabs(x)
c = n*x

if x <= n:
    ln = math.log(a, 10)
    y = ln - n
    print(y)
else:
    y = math.cos(c)
    print(y)