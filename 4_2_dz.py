# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


n = int(input('Введите натуральное число: '))

y = 2
while n > 1:
        if n % y == 0:
                n = n / y
                print(y)
        else:
                y = y + 1
