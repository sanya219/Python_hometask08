# Задача 1. Дано натуральное число N. Найдите значение выражения: N + NN + NNN
# N может быть любой длины.
# N = 132: 132 + 132132 + 132132132 = 132264396
def Task1():
    num = input("Введите число N: ")
    length = len(num)
    num = int(num)
    result = 3 * num + 2 * num * 10 ** length + num * 10 ** (length * 2)
    print(f"{num} + {num}{num} + {num}{num}{num} = {result}")
Task1()