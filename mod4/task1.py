def analyze_numbers(input_string):
    numbers = list(map(int, input_string.split()))
    if len(set(numbers)) == 1:
        return "Все числа равны"
    elif len(set(numbers)) == len(numbers):
        return "Все числа разные"
    else:
        return "Есть равные и неравные числа"

input_string = input("Введите числа через пробел: ")
result = analyze_numbers(input_string)
print(result)
