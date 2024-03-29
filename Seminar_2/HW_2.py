from fractions import Fraction

def process_fractions(frac1_str, frac2_str):
    # Преобразуем дроби из строк в числа
    num1, denom1 = map(int, frac1_str.split("/"))
    num2, denom2 = map(int, frac2_str.split("/"))

    # Вычисляем сумму дробей
    sum_frac_num = num1 * denom2 + num2 * denom1
    sum_frac_denom = denom1 * denom2
    sum_frac = (sum_frac_num, sum_frac_denom)

    # Вычисляем произведение дробей
    prod_frac_num = num1 * num2
    prod_frac_denom = denom1 * denom2
    prod_frac = (prod_frac_num, prod_frac_denom)

    return sum_frac, prod_frac, Fraction(num1, denom1), Fraction(num2, denom2)

# Пример использования функции
frac1 = "1/2"
frac2 = "1/3"

sum_frac, prod_frac, frac1_frac, frac2_frac = process_fractions(frac1, frac2)

print(f"Сумма дробей: {sum_frac[0]}/{sum_frac[1]}")
print(f"Произведение дробей: {prod_frac[0]}/{prod_frac[1]}")
print(f"Сумма дробей: {frac1_frac + frac2_frac}")
print(f"Произведение дробей: {frac1_frac * frac2_frac}")