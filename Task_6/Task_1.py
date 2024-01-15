"""Вы работаете над разработкой программы для проверки корректности даты, введенной пользователем.
На вход будет подаваться дата в формате "день.месяц.год". Ваша задача - создать программу, которая проверяет,
является ли введенная дата корректной или нет.
Ваша программа должна предоставить ответ "True" (дата корректна) или "False" (дата некорректна) в зависимости
от результата проверки.
"""
date_to_prove = 15.4.2023

def number_data(date_to_prove):
    test = date_to_prove.split(".")
    day_data = int(test[0])
    month_data = int(test[1])
    year_data = int(test[2])

    if day_data == 0 or month_data == 0 or year_data == 0:
        print(False)
    elif day_data <= 0 or month_data <= 0 or year_data <= 0:
        print(False)
    else:
        if month_data == 1 and day_data <= 31:
            print(True)
        elif month_data == 2 and day_data <= 28 or year_data % 4 == 0 and month_data == 2 and day_data <= 29:
            print(True)
        elif month_data == 3 and day_data <= 31:
            print(True)
        elif month_data == 4 and day_data <= 30:
            print(True)
        elif month_data == 5 and day_data <= 31:
            print(True)
        elif month_data == 6 and day_data <= 30:
            print(True)
        elif month_data == 7 and day_data <= 31:
            print(True)
        elif month_data == 8 and day_data <= 31:
            print(True)
        elif month_data == 9 and day_data <= 30:
            print(True)
        elif month_data == 10 and day_data <= 31:
            print(True)
        elif month_data == 11 and day_data <= 30:
            print(True)
        elif month_data == 12 and day_data <= 31:
            print(True)
        else:
            print(False)


number_data(date_to_prove)
