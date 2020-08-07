def declin(numeral, name): #Функция для выбора склонения
    num = numeral % 10
    mass = [2, 3, 4], [12, 13, 14]
    if num == 1 and numeral != 11: #Для отсеивания числа 11 и попаданий 1
        return name[0]
    if num in mass[0] and ((numeral%100) in mass[1]) == False: #Для отсеивания чисел 12, 13, 14 и попаданий 2, 3, 4
        return name[1]
    else:
        return name[2]

dec = ['час', 'часа', 'часов'], ['минута', 'минуты', 'минут'], ['секунда', 'секунды', 'секунд']
data_output = ''

try:
    time = int(input('Введите кол-во секунд: '))
except ValueError:
    print('Нужно вводить целое число!')
    time = int(input('Введите кол-во секунд ещё раз: '))

data_time = [time // 3600, (time % 3600) // 60, ((time % 3600) % 60)]

for it, i in enumerate(data_time):
    if i > 0:
        data_output = data_output + str(i) + ' ' + declin(i, dec[it]) + ' '

print(data_output)
