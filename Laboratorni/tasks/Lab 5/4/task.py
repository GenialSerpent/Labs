# Нехай x0 = x1 = 1,xi = x(i-1)+2x(i-2), де i=2,3,.... Визначити xn

n = int(input('n = '))
a = 1   #x0
b = 1   #x1
c = 1
x = 0

while c < n:
    x = b + 2 * a
    a = b
    b = x
    c += 1
print('xn = {0}'.format(x))
