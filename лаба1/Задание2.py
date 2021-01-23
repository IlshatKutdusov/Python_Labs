import math

print('Дано:')
r1 = int(input('R1 = '))
r2 = int(input('R2 = '))
s1 = round(math.pi * r1**2,2) # площадь 1 круга
s2 = round(math.pi * r2**2,2) # площадь 2 круга
if (r1 > r2): # площадь кольца
    s3 = s1 - s2
else :
    s3 = s2 - s1
print('Решение:')
print('Площадь круга1 = ',s1)
print('Площадь круга2 = ',s2)
print('Площадь кольца = ',s3)
