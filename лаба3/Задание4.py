print('Дано:')
n = int(input('N = '))
p = 2
print('Решение:')
if (n < 1):
    print('! N >= 1 !')
else:
    s = [] #список
    k7 = [] #список кратных 7
    i = 1
    while i <= n: #список чисел от 1 до n
        s.append(i)
        if (i%7 == 0): #список чисел от 1 до n кратных 7
            k7.append(i)
        i = i + 1
    print('Исходный список:', s)
    print('a)', k7)
    j = 0
    while j <= n: #получение списка простых чисел
        i = 0
        while i < len(s): #удаление чисел кратных р
            if s[i]%p == 0:
                if (s[i] != p):
                    del s[i]
            i = i + 1
        i = 0
        while i < len(s): #изменение р
            if (s[i] > p):
                p = s[i]
                i = len(s)
            i = i + 1
        if (s[len(s)-1] == p): #возможность дальнейшего удаления чисел
            j = n
        j = j + 1
    print('б)', s)
    s7 = [] #список все простых чисел кратных 7
    i = 0
    while i < len(s): #список всех простых чисел от 1 до n кратных 7
        if (s[i]%7 == 0):
            s7.append(s[i])
        i = i + 1
    print('в)', s7)

