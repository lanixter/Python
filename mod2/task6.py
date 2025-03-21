binary_string = input().strip()
count_0 = binary_string.count('0')
count_1 = binary_string.count('1')
if count_0 == count_1:
    print("yes")
else:
    print("no")
