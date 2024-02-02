from datetime import datetime
import warnings

warnings.filterwarnings('ignore')

# Введите ваше решение ниже


class MyStr(str):
    def __new__(cls, value, author):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = datetime.now().strftime('%Y-%m-%d %H:%M')
        return instance

    def __str__(self):
        return f"{super().__str__()} (Автор: {self.author}, Время создания: {self.time})"

    def __repr__(self):
        return f"MyStr({super().__repr__()}, {repr(self.author)})"


my_string = MyStr("Заключительный текст", "Достоевский")
print(repr(my_string))
