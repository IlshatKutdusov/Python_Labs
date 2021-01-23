def y(x,n): #собственная функция рассчитывающая сумму всех n-ых членов
    i = 0
    y = 0
    minus = 1
    while i <= n:
        xi = 1
        j = 1
        while j <= 2*i+1: #возведение в степень
            xi = xi * x
            j = j + 1
        y = y + ((-1)*minus) / ((2*i+1) * xi)
        minus = -minus
        i = i + 1
    return y
import math

print('Дано:')
x = int(input('х = '))
n = int(input('n = '))
print('Решение:')
if ((x<-1)and(n>=0)):
    print('y(x) = ', y(x,n) - (math.pi / 2)) #воспользовались собственной функцией
else:
    print('!!! x < -1 and n >= 0 !!!') #результат проверки x и n
