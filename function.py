from functools import reduce

# 13.1
# a = int(input())
# b = int(input())
# c = int(input())
#
# def max_value(num1, num2, num3):
#     return max(num1, num2, num3)
#
# print(max_value(a, b, c))


# 13.2
# ls = [int(i) for i in input().split()]
#
# def sum_of_values(nums_list):
#     return sum(ls)
# print(sum_of_values(ls))


# 13.3
# ls = [int(i) for i in input().split()]
#
# def mult_of_values(nums_list):
#     mult = 1
#     for i in ls:
#         mult *= i
#
#     return mult
#
# print(mult_of_values(ls))


# def mult_of_values(*nums):
#     mult = 1
#     print(nums)
#     for num in nums:
#         mult *= num
#     return mult
#
# print(mult_of_values(2, 4, 1, 6))


# def print_kwargs(**kwargs):
#     for k, v in kwargs.items():
#         print("Значение для {} является {}".format(k, v))
#
# print(print_kwargs(arg1="blabla", arg2='hoho'))


# def summ(a, b):
#     return a + b
#
# summ = lambda a, b: a + b
# print(type(summ))
# print(summ(3, 4))


# 13.4
# Создайте функцию count_letters,
# которая принимает на вход фразу и
# подсчитывает, какое количество в ней
# строчных(down) и заглавных (up) букв.
# Функция должна вывести на экран
# информацию о найденных буквах в
# определенном формате.
# Количество заглавных символов: up
# Количество строчных символов: down

# def count_letters(phrase):
#     up = 0
#     down = 0
#     for i in phrase:
#         if i.isupper():
#             up += 1
#         elif i.islower():
#             down += 1
#     return f'Количество заглавных символов:{up}'\
#             f'Количество строчных символов:{down}'
#
# word = input()
# print(count_letters(word))

# 13.5

# Напишите
# функцию count_args,
# которая
# принимает произвольное
# количество аргументов.
# Данная функция должна
# возвращать количество
# переданных ей на вход
# аргументов


# def count_args(*args):
#     return len(args)
#
#
# print(count_args(2, 'wedf', 5.4, True))
#
#


# 13.6
# Напишите
# функцию info_kwargs,
# которая
# принимает произвольное
# количество
# именованных аргументов.
# Функция info_kwargs должна
# распечатать именованные
# аргументы в каждой новой
# строке в виде пары
# <Ключ> = <Значения>, причем
# ключи должны следовать в
# алфавитном порядке

# def info_kwargs(**kwargs):
#     for k, v in sorted(kwargs.items()):
#         print(f'{k} --- {v}')
#
# info_kwargs(hoho=1, lolo=2, yoyo=3, qwerty=5)


# def getTalk(type="shout"):
#     # Мы определяем функции прямо здесь
#     def shout(word="да"):
#         return word.capitalize() + "!"
#
#     def whisper(word="да"):
#         return word.lower() + "..."
#
#     # Затем возвращаем необходимую
#     if type == "shout":
#         return shout
#     else:
#         return whisper
# print(getTalk("shout")('Hello'))
# print(getTalk("whisper")('By'))


# def mult(num):
#     return num * 2
# elems = [2, 5, 7]
# elems_x2 = list(map(mult, elems))
#
#
# print(elems_x2)


# a, b = map(int, input().split())
# print(a, b)

# def even_num(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
# nums = [1, 2, 3, 4, 5, 6, 7]
# filtered = list(filter(even_num, nums))
# print(filtered)


# nums = [1, 2, 3, 4, 5, 6, 7]
# filtered = list(filter(lambda i: i%2 == 0, nums))
# print(filtered)


# nums = [1, 2, 3, 4, 5]
# mult = reduce(lambda x, y: x * y, nums)
# print(mult)


# nums = [1, 2, 3, 4, 5]
# mult = reduce(lambda x, y: x * y, nums, 0)
# print(mult)

# 13.7
# Напишите программу,
# которая возводит в куб
# каждое число из
# полученного списка чисел
# пользуясь при этом
# функциями map и lambda.

# elems = [int(i) for i in input().split()]
# new_elems = list(map(lambda i: i**3, elems))
#
# print(new_elems)


# 13.8
# На вход программа получает
# список, состоящий из
# отрицательных, положительных
# чисел и нулей
# При помощи функций filter, len,
# lambda определить сколько в
# списке чисел отрицательных
# значений, сколько нулей и
# сколько положительных.

# elems = [int(i) for i in input().split()]
# neg = len(list(filter(lambda i: i < 0, elems)))
# pos = len(list(filter(lambda i: i > 0, elems)))
# zero = len(list(filter(lambda i: i == 0, elems)))

# 13.9
# На вход программа получает 2
# числа через пробел, не
# иначе! Выведите сумму этих
# двух чисел.
# Воспользуйтесь функцией
# map


# a, b = map(int, input().split())
# print(a + b)


# def my_shiny_new_decorator(a_function_to_decorate):
#     def the_wrapper_around_the_original_function():
#         print("Я - код, который отработает до вызова функции")
#
#         a_function_to_decorate()
#
#         print("А я - код, срабатывающий после")
#
#     return the_wrapper_around_the_original_function
#
#
# @my_shiny_new_decorator
# def a_stand_alone_function():
#     print("Я простая одинокая функция, ты ведь не посмеешь меня изменять?..")
#
#
# a_stand_alone_function()

# 13.10
# Дано натуральное число N и
# последовательность из N
# элементов. Требуется вывести
# эту последовательность в
# обратном порядке, используя
# рекурсию

# lens = int(input('Введите количество элементов: '))
#
# def rec(i):
#     if i < lens:
#         x = int(input('Введите число: '))
#         rec(i+1)
#         print(x)
#
# rec(0)

# n = int(input())
# ls = [int(input()) for i in range(n)]
#
# def rev(n, ls):
#     if n != 0:
#         print(ls[n-1])
#         rev(n - 1, ls)
#
# (rev(n, ls))


# 13.11
# Напишите декоратор к функции
# деления, который меняет
# местами делимое и делитель


# def decor_div(func):
#     def ab(a, b):
#         return b / a
#         func(a, b)
#
#     return ab
#
#
# @decor_div
# def div(a, b):
#     return a / b
#
# print(div(2, 4))


# 13.12
# Пользователь делает вклад N
# рублей на X лет под 10 %
# годовых, т.е. каждый год размер
# его вклада увеличивается на
# 10%. Напишите функцию,
# которая возвращает
# накопленную сумму.


# def save(money, years):
#     i = 1
#     while i <= years:
#         money *= 1.1
#         i += 1
#     return money
#
# print(save(10, 2))






