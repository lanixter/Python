input_line = input().strip()
words = ''
last_letters = ''

for char in input_line:
    if char != ' ':
        words += char
    else:
        last_letters += words[-1]
        words = ''

last_letters += words[-1]
print(last_letters)
