# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input("Введите кол-во элементов первого множества: "))
array_n = {int(i) for i in input("Введите значения первого множества: ").split()}
m = int(input("Введите кол-во элементов второго множества: "))
array_m = {int(i) for i in input("Введите значения второго множества: ").split()}
print(sorted(array_n & array_m))