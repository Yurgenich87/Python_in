"""Дан список повторяющихся элементов lst. Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
"""
from collections import Counter

lst = [1, 2, 3, 4, 5]

counter = Counter(lst)
duplicates = [element for element, count in counter.items() if count > 1]

print(duplicates)
