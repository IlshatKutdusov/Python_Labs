print('Дано:')
a = int(input('A = '))
a1 = a // 100 # 1-ая цифра трехзначного числа
a2 = (a % 100) // 10 # 2-ая цифра трехзначного числа
a3 = a % 10 # 3-яя цифра трехзначного числа
b = a2 * 100 + a3 * 10 + a1 # искомое число
print('Решение:')
print('Число = ', b)
