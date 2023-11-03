a = 4
b = 4
c = 4

if (a + b > c) and (b + c > a) and (c + a > b):
    print("Треугольник существует")
    if a != b and b != c and a != c:
        print("Треугольник разносторонний")
    elif a == b and b == c and a == c:
        print("Треугольник равносторонний")
    else:
        print("Треугольник равнобедренный")
else:
    print("Треугольник не существует")

