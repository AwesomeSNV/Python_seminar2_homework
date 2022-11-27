#Реализуйте алгоритм перемешивания списка.

n = int(input('Введите размер массива: '))
my_lst=[]
for i in range(n):
    num=int(input('Введите элемент массива(целое число): '))
    my_lst.append(num)
print(my_lst)

#with random

import random
random.shuffle(my_lst)    
print(my_lst)