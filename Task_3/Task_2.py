"""В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
Слова разделяются пробелами. Такие слова как don t, it s, didn t итд (после того, как убрали знак препинания апостроф) считать двумя словами.
Цифры за слова не считаем.
Отсортируйте по убыванию значения количества повторяющихся слов.
"""

from collections import Counter
import re
text = 'Hello world. Hello Python. Hello again.'


words = re.findall(r'\b[^\d\W]+\b', text.lower())

word_counts = Counter(words)

duplicates = [(word, count) for word, count in word_counts.items() if count >= 1]
sorted_list = sorted(duplicates, key=lambda x: x[1], reverse=True)
print(sorted_list)
