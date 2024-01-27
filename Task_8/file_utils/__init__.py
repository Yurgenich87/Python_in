




code_to_write = '''
import os
import json
import csv
import pickle

def get_dir_size(directory):
    total_size = 0
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file():
                total_size += entry.stat().st_size
            elif entry.is_dir():
                total_size += get_dir_size(entry.path)
    return total_size

def save_results_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

def save_results_to_csv(data, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def save_results_to_pickle(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)

def traverse_directory(directory):
    files_list = []
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file():
                files_list.append(entry.name)
            elif entry.is_dir():
                files_list.extend(traverse_directory(entry.path))
    return files_list
'''

with open("__init__.py", "w") as init_file:
    init_file.write(code_to_write)
