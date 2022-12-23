#2. Напишите программу, которая найдёт произведение пар чисел списка.
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
array1 = [int(i) for i in input('Введите элементы через пробел ').split()]
array2 = []
for i in range(len(array1)//2):
    array2.append(array1[i] * array1[len(array1)-1-i])
if len(array1) % 2 !=0:
    array2.append(array1[len(array1)//2] ** 2)
print(array1)
print(array2)