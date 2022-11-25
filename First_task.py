#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

#Пример:

#- 6782 -> 23
#- 0,56 -> 11

#Methods

def Sum_Numbers(num):
    result = 0
    for i in str(num):
        if i != ".":
            result += int(i)
    return result

num = float(input('Введите вещественное число: '))
print(f'Сумма цифр во введенном числе равняется: {Sum_Numbers(num)}')