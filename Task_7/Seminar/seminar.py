import os
from itertools import cycle
from random import randint, uniform
from itertools import cycle
import random

DIGITS_MIN = -1000
DIGITS_MAX = 1000


# Task_1
def append_digits(file_name: str, number_str: int):
    """generation of random numbers from -1000 to 1000, output: int | float"""
    with open(file_name, "a", encoding="utf-8") as file:
        for i in range(number_str):
            file.write(f"{randint(DIGITS_MIN, DIGITS_MAX + 1)} | {round(uniform(DIGITS_MIN, DIGITS_MAX + 1), 2)}\n")


# Task_2
def generate_name(file_name: str, counter: int):
    """Pseudo-name generation"""
    with open(file_name, "a", encoding="utf-8") as file:
        while counter:
            word = ''
            glass = 'аеёиоуыэюя'
            for i in range(1, random.randint(5, 8)):
                letter = random.choice('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
                word += letter
            if any(char in glass for char in word.lower()):
                file.write(word.capitalize() + '\n')
                counter -= 1
            else:
                continue


# Task_3
def open_read_files(file1_path, file2_path, result_file_path):
    with open(file1_path, 'r', encoding='utf-8') as file1, \
            open(file2_path, 'r', encoding='utf-8') as file2, \
            open(result_file_path, 'a', encoding='UTF-8') as file_result:
        lines_file1 = [line.strip() for line in file1.readlines()]
        lines_file2 = [line.strip() for line in file2.readlines()]
        max_length = max(len(lines_file1), len(lines_file2))

        for i in range(max_length):
            name = lines_file1[i % len(lines_file1)].split()[0]
            number = lines_file2[i % len(lines_file2)].split('|')

            if float(number[0]) * float(number[1]) < 0:
                data = abs(float(number[0]) * float(number[1]))
                name = name.lower()
                print(name)
            else:
                data = int(float(number[0]) * float(number[1]))
                name = name.upper()

            file_result.write(name + " " + str(data) + "\n")


# Task_4
def generation_files(extension, min_length, max_length, min_digit_byte, max_digit_byte, quantity):
    """Generation random files"""
    while quantity:
        word = ''
        glass = 'aeiou'
        for i in range(1, random.randint(min_length, max_length)):
            letter = random.choice('abcdefghijklmnopqrstuvwxyz')
            word += letter
        if any(char in glass for char in word.lower()):
            quantity -= 1
            word = f"{word}{extension}"
            file_size = random.randint(min_digit_byte, max_digit_byte)
            random_byte = os.urandom(file_size)
            with open(word, 'wb') as file:
                file.write(random_byte)
        else:
            continue


def generation_extension(list_extension, number_files):
    """Generation random files"""
    extension = list_extension.split(', ')
    for i in range(number_files):
        extension_result = f'.{extension[i % len(extension)]}'
        generation_files(extension_result, 7, 31, 256, 4096, 1)




if __name__ == '__main__':
    # append_digits('Digits_int_float', 12)
    # generate_name('Pseudo_name.txt', 10)
    # open_read_files('Pseudo_name.txt', 'Digits_int_float', 'result.txt')
    # generation_files('.txt', 7, 31, 256, 4096, 5)
    generation_extension('txt, doc, py, bin', 3)
