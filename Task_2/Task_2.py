"""На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
Напишите программу, которая должна возвращать сумму и произведение дробей. Дроби упрощать не нужно.
Для проверки своего кода используйте модуль fractions.
"""

frac1 = "1/2"
frac2 = "1/3"

# Введите ваше решение ниже

from fractions import Fraction


def add_and_multiply(frac1, frac2):
    # Разбиваем строки на числитель и знаменатель для каждой дроби
    num1, denom1 = map(int, frac1.split('/'))
    num2, denom2 = map(int, frac2.split('/'))

    # Вычисление суммы дробей
    sum_num = num1 * denom2 + num2 * denom1
    sum_denom = denom1 * denom2

    # Вычисление произведения дробей
    product_num = num1 * num2
    product_denom = denom1 * denom2

    return (f"{sum_num}/{sum_denom}", f"{product_num}/{product_denom}")


sum_result, product_result = add_and_multiply(frac1, frac2)
print(f"Сумма дробей: {sum_result}")
print(f"Произведение дробей: {product_result}")


fracF1 = Fraction(frac1)
fracF2 = Fraction(frac2)
# Арифметические операции с дробями
result = fracF1 + fracF2
multiplication = fracF1 * fracF2
print(f"Сумма дробей: {result}")
print(f"Произведение дробей: {multiplication}")

