#5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
array = [0, 1]
n = int(input())
for i in range(1, n):
    array.append(array[i] + array[i-1])
print(array)
while n != 0:
    array.insert(0, array[1] - array[0])
    n -=1
print(array)