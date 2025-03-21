def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

input_string = input("Введите a и b через пробел: ")
a, b = map(int, input_string.split())
result = gcd(a, b)
print(f"Наибольший общий делитель чисел {a} и {b} равен {result}")
