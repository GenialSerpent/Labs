'''
Перевірити справедливість рівності при заданій точності епсіон:
ln(1-x)=-[x+(x**2/2)+(x**3/3)+...+(x**n/n), x<1
'''
import math
x = int(input('x<1 = '))
e = int(input('епсіон = '))
b = 1
sum = 0
while abs(x/b) > e:
    sum += x/b
    x *= x
    b += 1
print(sum)
if math.log(1-x, 10) == -sum:
    print('Рівність справедлива')
else:
    print('Рівність несправедлива')