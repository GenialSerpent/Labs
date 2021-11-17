'''
Трикутник задається координатами своїх вершин на площині:A(x1,y1), B(x2,y2), C(x3,y3).
Визначити, чи є цей трикутник прямокутним.
'''
import math

x1 = float(input('x1 = '))
x2 = float(input('x2 = '))
x3 = float(input('x3 = '))
y1 = float(input('y1 = '))
y2 = float(input('y2 = '))
y3 = float(input('y3 = '))

ab = (math.sqrt(((x1 - x2)**2)+((y1 - y2)**2)))
bc = (math.sqrt(((x2 - x3)**2)+((y2 - y3)**2)))
ac = (math.sqrt(((x1 - x3)**2)+((y1 - y3)**2)))

if ab**2 == bc**2 + ac**2 or ac**2 == ab**2 + bc**2 or bc**2 == ab**2 + ac**2:
    print('Трикутник прямокутний')
else:
    print('Трикутник не прямокутний')

