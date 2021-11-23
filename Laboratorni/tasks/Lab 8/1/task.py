'''
За даними дійсними числами a і b  обчислити
u=f(a,b)+f(2,a)+2, де
        {x**3+(x**2+y**4)**1/2,          x>0 and y>0
f(x,y)= {(x**2-2*x+x**1/2)/(x**3)**1/5,  x>0 and y<0
        {sin(x*y),                       else
'''
from math import sin
def f(x, y):
    if x > 0 and y > 0:
        n = x ** 3 + (x ** 2 + y ** 4) ** 1 / 2
    elif x > 0 and y < 0:
        n =(x ** 2 - 2 * x + x ** 1 / 2) / (x ** 3) ** 1 / 5
    else:
        n = sin(x*y)
    return n

a = float(input('a= '))
b = float(input('b= '))

u = f(a, b) + f(2, a) + 2
print('u= {0}'.format(u))