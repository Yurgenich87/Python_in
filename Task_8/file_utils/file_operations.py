import os
import json
import csv
import pickle


def get_dir_size(directory):
    total_size = 0
    for root, dirs, files in os.walk(directory):
        for name in files:
            file_path = os.path.join(root, name)
            total_size += os.path.getsize(file_path)
        for d in dirs:
            total_size += get_dir_size(os.path.join(root, d))
    return total_size


def traverse_directory(directory):
    results = []

    for root, dirs, files in os.walk(directory):
        for name in files:
            file_path = os.path.join(root, name)
            size = os.path.getsize(file_path)
            results.append({'Path': file_path, 'Type': 'File', 'Size': size})

        for name in dirs:
            dir_path = os.path.join(root, name)
            size = get_dir_size(dir_path)
            results.append({'Path': dir_path, 'Type': 'Directory', 'Size': size})

    return results


def save_results_to_json(results, output_file):
    with open(output_file, 'w') as json_file:
        json.dump(results, json_file, indent=2)


def save_results_to_csv(results, output_file):
    with open(output_file, 'w', newline='') as csv_file:
        fieldnames = ['Path', 'Type', 'Size']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for result in results:
            writer.writerow(result)


def save_results_to_pickle(results, output_file):
    with open(output_file, 'wb') as pickle_file:
        pickle.dump(results, pickle_file)
