def to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary


def to_octal(n):
    if n == 0:
        return "0"
    octal = ""
    while n > 0:
        octal = str(n % 8) + octal
        n //= 8
    return octal


def to_hexadecimal(n):
    hex_chars = "0123456789ABCDEF"
    if n == 0:
        return "0"
    hexadecimal = ""
    while n > 0:
        hexadecimal = hex_chars[n % 16] + hexadecimal
        n //= 16
    return hexadecimal

input_value = input().strip()
if not input_value.isdigit() or int(input_value) <= 0:
    print("Неверный ввод")
else:
    number = int(input_value)
    binary_representation = to_binary(number)
    octal_representation = to_octal(number)
    hexadecimal_representation = to_hexadecimal(number)
    print(binary_representation, octal_representation, hexadecimal_representation)
