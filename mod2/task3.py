input_line = input().strip()
a, b, c = 0, 0, 0
current_number = ''
index = 0

for char in input_line:
    if char != ' ':
        current_number += char
    else:
        if index == 0:
            a = int(current_number)
        elif index == 1:
            b = int(current_number)
        elif index == 2:
            c = int(current_number)

        current_number = ''
        index += 1

if index == 0:
    a = int(current_number)
elif index == 1:
    b = int(current_number)
else:
    c = int(current_number)
if (a >= b and a <= c) or (a <= b and a >= c):
    middle = a
elif (b >= a and b <= c) or (b <= a and b >= c):
    middle = b
else:
    middle = c
print(middle)
