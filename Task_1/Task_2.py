num = 100000

# Введите ваше решение ниже

if num <= 1 or num >= 100001:
    print("Число должно быть больше 1 и меньше 100000")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Простое")
    else:
        print("Не является простым")
