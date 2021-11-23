'''
Використовуючи відповідну підпрограму знаходження g(i), обчислити значення виразу s=g(7)+g(9), lt
g(i)=sin(g(i-1)+cos(g(i-2))), g(0)=9, g(1)=35
'''
from math import sin
from math import cos

def g(i):
    x = 9
    y = 35
    z = 1
    n = 0
    while z < i:
        n = sin(y+cos(x))
        x = y
        y = n
        z += 1
    return n
print('g(7)= {0}'.format(g(7)))
print('g(9)= {0}'.format(g(9)))

s = g(7) + g(9)
print('s = {0}'.format(s))