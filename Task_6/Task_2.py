queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]


def check_queens(queens):
    pairs = []
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            pairs.append((queens[i], queens[j]))
    return pairs

def check_queens(queens):
    pairs = []
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            pairs.append((queens[i], queens[j]))
    for pair in pairs:
        if not is_attacking(pair[0], pair[1]):
            return False
    return True


def is_attacking(q1, q2):
    # Проверка на атаку
    if q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1]):
        return False  # Ферзи бьют друг друга, возвращаем False
    return True  # Ферзи не бьют друг друга, возвращаем True
