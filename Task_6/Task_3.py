import random

def is_attacking(q1, q2):
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])

def generate_board():
    queens = []
    max_attempts = 1000  # Ограничение на количество попыток вставки ферзя

    while len(queens) < 8:
        attempts = 0
        while attempts < max_attempts:
            queen = (random.randint(1, 8), random.randint(1, 8))
            if all(not is_attacking(queen, q) for q in queens):
                queens.append(queen)
                break
            attempts += 1
        else:
            # Если не удалось вставить ферзя после max_attempts попыток, начать заново
            queens = []

    return queens

def generate_boards(num_boards=4):
    board_list = []
    for _ in range(num_boards):
        board_list.append(generate_board())
    return board_list

board_list = generate_boards()
if len(board_list) != 4:
    print("Вы собрали не то количество комбинаций")
else:
    print("Отлично!")
