#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

read_file = open('file.txt', 'r', encoding='utf8')

array = []
for line in read_file:
    array.append(int(line))
N = array[0]
array.remove(N)

second_array = []
for i in range(-N, N+1):
    second_array.append(i)

count = 1
for i in array:
    count *= second_array[i]
print(count)

read_file.close()