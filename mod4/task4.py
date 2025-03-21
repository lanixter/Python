def can_form_palindrome(s):
    from collections import Counter
    count = Counter(s)

    odd_count = sum(1 for value in count.values() if value % 2 != 0)

    if odd_count > 1:
        return None

    half_palindrome = []
    middle_char = ''

    for char, freq in count.items():
        if freq % 2 == 1:
            middle_char = char
        half_palindrome.extend(char * (freq // 2))

    half_palindrome = ''.join(half_palindrome)

    return half_palindrome + middle_char + half_palindrome[::-1]


input_string = input("Введите строку: ")
palindrome = can_form_palindrome(input_string)

if palindrome:
    print(f"Составленный палиндром: {palindrome}")
else:
    print("Палиндром составить невозможно")
