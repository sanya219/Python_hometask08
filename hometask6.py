import random
from math import gcd

# Задача 1. Дано натуральное число N. Найдите значение выражения: N + NN + NNN
# N может быть любой длины.
# N = 132: 132 + 132132 + 132132132 = 132264396
def Task1():
    print("Задача 1:")
    num = input("Введите число N: ")
    length = len(num)
    num = int(num)
    result = 3 * num + 2 * num * 10 ** length + num * 10 ** (length * 2)
    print(f"{num} + {num}{num} + {num}{num}{num} = {result}")
Task1()

# Задача 2. Задан массив из случайных цифр на 15 элементов. На вход подаётся трёхзначное натуральное число. 
# Напишите программу, которая определяет, есть в массиве последовательность из трёх элементов, 
# совпадающая с введённым числом.
# [0, 5, 6, 2, 7, 7, 8, 1, 1, 9] - 277 -> да
# [4, 4, 3, 6, 7, 0, 8, 5, 1, 2] - 812 -> нет
def Task2():
    print("\nЗадача 2:")
    numbers = [random.randint(1, 9) for _ in range(15)]
    print("Исходный массив: ", numbers)
    num = input("Введите трёхзначное натуральное число: ")
    numbers_array = "".join(str(x) for x in numbers)
    if num in numbers_array:
        print("Последовательность существует.")
    else:
        print("Последовательность не существует.")
Task2()

# Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.
def Task3():
    print("\nЗадача 3:")
    max_denominator = 11
    fractions = simple_fractions(max_denominator)
    print("Несократимые дроби между 0 и 1 с знаменателем не больше", max_denominator)
    for fraction in fractions:
        print(f"{fraction[0]}/{fraction[1]}")

def is_coprime(a, b):
    return gcd(a, b) == 1

def simple_fractions(max_denominator):
    fractions = []
    for denominator in range(1, max_denominator + 1):
        for numerator in range(1, denominator):
            if is_coprime(numerator, denominator):
                fractions.append((numerator, denominator))
    return fractions

Task3()
