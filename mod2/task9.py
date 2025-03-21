input_number = input().strip()
cleaned_number = ''

for char in input_number:
    if char.isdigit() or char == '+':
        cleaned_number += char

print(cleaned_number)
