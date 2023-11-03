num = 9
def is_prime(num):
    if num <= 1 or num > 100000:
        return "Число должно быть больше 1 и меньше 100000"

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return f"{num} является составным числом"
    return f"{num} является простым числом"

print(is_prime(num))
