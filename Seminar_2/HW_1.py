num = 123456
def to_hex(num):
    hex_digits = "0123456789ABCDEF"
    hex_str = ""
    while num > 0:
        hex_str = hex_digits[num % 16] + hex_str
        num = num // 16
    return hex_str

print(f"Шестнадцатеричное представление числа:", to_hex(num))
print(f"Проверка результата:", hex(num))