import argparse

parser = argparse.ArgumentParser(description='My first argument parser')
parser.add_argument('numbers', metavar='N', type=float, nargs='*', help='press some numbers')
args = parser.parse_args()
print(f'Получили экземпляр класса Namespace: {args = }')
print(f'У Namespace работает точечная нотация: {args.numbers = }')
print(f'Объекты внутри могут быть любыми: {args.numbers[1] = }')