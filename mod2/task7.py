input_line = input().strip()
s, char_to_count = '', ''
index = 0
for char in input_line:
    if char == ',':
        index += 1
    else:
        if index == 0:
            s += char
        elif index == 1:
            char_to_count += char
count = 0
for char in s:
    if char == char_to_count:
        count += 1
    else:
        break

print(count)
