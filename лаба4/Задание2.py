def gcd(m, n): #рекурсивная функция, алгоритм Евклида
    if (m != 0):
        if (m < n):
            return gcd(n, m)
        else:
            return gcd(m - n, n)
    return n

print('Дано:')
nf = float(input('N = '))
mf = float(input('M = '))
print('Решение: ')
if (nf % round(nf) != 0)or(mf % round(mf) != 0):
    #проверка: являются ли n и m целыми
    print('!!! n,m - целые числа !!!')
else:
    n = int(nf)
    m = int(mf)
    if (n > 0)and(m > 0): #проверка на положительность n и m
        print('(Рекурсия)НОД =', gcd(m, n))
        while m != n:
            if (m != 0):
                if (m < n):
                    c = n
                    n = m
                    m = c
                else:
                    m = m - n
            else:
                m = n
        print('(Цикл)НОД =', n)
                
    else:
        print('!!! n,m > 0 !!!')
