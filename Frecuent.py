mas = []
data_string = []


length = int(input('Введите длинну массива: '))
if length < 1 or length > 300000:
    print('Длинна массива должна соответствовать условию 1 ≤ n ≤ 300 000')
    exit(0)

data = input('Введите ' + str(length) + ' элементов массива через пробел: ')
data = data.split(' ')

try:
    for i in range(0, length+1):
        if int(data[i]) >= 0 or int(data[i]) <= 1000000000:
            data_string.append(int(data[i]))
        else:
            print('Каждое число должно быть целым и соответсвтовать условию 0 ≤ ai ≤ 1 000 000 000')
            exit(0)
except ValueError:
    print('Можно вводить только числа...')
    exit(0)

print('Вы ввели массив: ', end=' ')
print(data_string)

mas = [data_string[0], data_string.count(data_string[0])]
for i in data_string:
    if data_string.count(i) > mas[1]:
        mas[0] = i
        mas[1] = data_string.count(i)

if mas[0]>1:
    print('Число ' + str(mas[0]) + ' самое часто встречающееся в массиве' )
else:
    print('Все числа в массиве не повторяются...')