import math

print('Дано:')
a = int(input('A = '))
b = int(input('B = '))
c = math.hypot(a,b) # находим гипотензу с через а и b
p = a + b + c # находим периметр
print('Решение:', '\nC = ', c, '\nP = ', p)
