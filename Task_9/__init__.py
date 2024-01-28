
code_to_write = '''
import csv
import json
import math
import random


def generate_csv_file(file_name, rows):
    with open(file_name, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for _ in range(rows):
            row_data = [random.randint(100, 1000) for _ in range(3)]
            csv_writer.writerow(row_data)


def find_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        return None
    elif discriminant == 0:
        root = -b / (2 * a)
        return root
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2


def save_to_json(func):
    def wrapper(*args, **kwargs):
        # Читаем данные из CSV-файла
        with open(args[0], 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            data = [list(map(int, row)) for row in csv_reader]

        # Вычисляем корни и сохраняем результаты в JSON
        results = []
        for params in data:
            roots = func(*params)
            result_entry = {'parameters': params, 'result': roots}
            results.append(result_entry)

        with open('results.json', 'w') as jsonfile:
            json.dump(results, jsonfile, indent=2)

    return wrapper


@save_to_json
def find_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        return None
    elif discriminant == 0:
        root = -b / (2 * a)
        return root
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2

'''

with open("__init__.py", "w") as init_file:
    init_file.write(code_to_write)
