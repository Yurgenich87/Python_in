"""Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""
file_path = "C:/Users/User/Documents/example.txt"

# Введите ваше решение ниже
def get_file_info(file_path):
    my_list = ()
    dot_index = file_path.rfind(".")  # находим позицию точки
    slash_index = file_path.rfind("/")  # находим позицию символа "/"
    address = file_path[:slash_index + 1:]
    name = file_path[slash_index + 1:dot_index:]
    expansion = file_path[dot_index::]
    # print(f"{address = }")
    # print(f"{name = }")
    # print(f"{expansion = }")
    my_list = (address, name, expansion)
    return my_list
