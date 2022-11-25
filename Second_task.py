#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

#Пример:

#- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

#Methods

def Multiply(n):
    if n == 1:
        return 1
    else:
        return n * Multiply(n-1)

num = int(input('Введите целое число: '))
mult_set=[]
for e in range(1, num + 1):
    mult_set.append(Multiply(e))

print(f'Произведения чисел от 1 до {num}: {mult_set}')