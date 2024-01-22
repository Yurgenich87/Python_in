from random import randint, uniform


def append_digits(number_str: int, file_name: str):
    with open(file_name, "a", encoding="utf-8") as file:
        for i in range(number_str):
            file.write(f"{randint(-1000, 1001)} | {round(uniform(-1000, 1001), 2)}\n")


append_digits(5, "test_file")

