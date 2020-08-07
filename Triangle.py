
try:
    num = int(input('Введите целое число: '))
except ValueError:
    print('Нужно ввести целое число!')
    num = int(input('Введите целое число ещё раз: '))

triangle = ''

if num > 0:
    for i in range(1, num+1):
        if i<10:
            print(triangle.rjust(num-i, ' ') + (str(i)+' ')*i)
        else:
            print(triangle.rjust(num - i, ' ') + str(i) * i)
else:
    print('Число должно быть больше 0')
