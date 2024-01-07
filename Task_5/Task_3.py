"""Создайте функцию генератор чисел Фибоначчи fibonacci.
https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8
"""


def fibonacci():
    my_list = [0, 1]
    numbers_fibonacci = 0
    for i in range(10):
        numbers_fibonacci = my_list[i] + my_list[i+1]
        my_list.append(numbers_fibonacci)
    my_iterator = iter(my_list)
    return my_iterator


f = fibonacci()
for i in range(10):
   print(next(f))
