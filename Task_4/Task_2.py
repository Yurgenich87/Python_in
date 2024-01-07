"""Напишите функцию key_params, принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ - значение переданного аргумента, а значение - имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
"""


def key_params(**kwargs):
    return {(str(value) if value is None or isinstance(value, (list, dict)) else value): key for key, value in kwargs.items()}


params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
print(params)
