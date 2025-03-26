def date_to_word(n):
    days = {
        1: "первое", 2: "второе", 3: "третье", 4: "четвертое", 5: "пятое",
        6: "шестое", 7: "седьмое", 8: "восьмое", 9: "девятое", 10: "десятое",
        11: "одиннадцатое", 12: "двенадцатое", 13: "тринадцатое", 14: "четырнадцатое",
        15: "пятнадцатое", 16: "шестнадцатое", 17: "семнадцатое", 18: "восемнадцатое",
        19: "девятнадцатое", 20: "двадцатое", 21: "двадцать первое", 22: "двадцать второе",
        23: "двадцать третье", 24: "двадцать четвертое", 25: "двадцать пятое",
        26: "двадцать шестое", 27: "двадцать седьмое", 28: "двадцать восьмое",
        29: "двадцать девятое", 30: "тридцатое", 31: "тридцать первое"
    }
    return days.get(n, "Неверный день")
def month_to_word(n):
    months = {
        1: "января", 2: "февраля", 3: "марта",
        4: "апреля", 5: "мая", 6: "июня",
        7: "июля", 8: "августа", 9: "сентября",
        10: "октября", 11: "ноября", 12: "декабря"
    }
    return months.get(n, "Неверный месяц")

def number_to_words(n):
    ones = [
        "", "первого", "второго", "третьего", "четвертого", "пятого", "шестого",
        "сельмого", "восьмого", "девятого", "десятого", "одинадцатого",
        "двенадцатого", "тринадцатого", "четырнадцатого", "пятнатцатого",
        "шестнадцатого", "семнадцатого", "восемнадцатого", "девятнадцатого"
    ]
    tens = [
        "", "", "двадцать", "тридцать", "сорок", "пятьдесят",
        "шестьдесят", "семьдесят", "восемьдесят", "девяносто"
    ]
    hundreds = [
        "", "сто", "двести", "триста", "четыреста",
        "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"
    ]

    result = ""
    if n >= 100:
        h = n // 100
        result += hundreds[h] + " "
        n %= 100
    if n < 20:
        result += ones[n]
    else:
        t = n // 10
        result += tens[t] + " "
        n %= 10
        result += ones[n]
    return result.strip()
def year_to_word(n):
    if n % 100 == 0:
        thousands = n // 1000
        hundreds_digit = (n % 1000) // 100
        if hundreds_digit == 0:
            ordinal_thousands = {
                1: "тысячного",
                2: "двухтысячного",
                3: "трёхтысячного",
                4: "четырёхтысячного"
            }
            return ordinal_thousands.get(thousands, number_to_words(thousands) + "тысячного")
        else:
            cardinal_thousands = {
                1: "тысяча",
                2: "две тысячи",
                3: "три тысячи",
                4: "четыре тысячи"
            }
            ordinal_hundreds = {
                1: "сотого",
                2: "двухсотого",
                3: "трёхсотого",
                4: "четырёхсотого",
                5: "пятисотого",
                6: "шестисотого",
                7: "семисотого",
                8: "восьмисотого",
                9: "девятисотого"
            }
            thousands_word = cardinal_thousands.get(thousands, number_to_words(thousands))
            hundreds_word = ordinal_hundreds.get(hundreds_digit, number_to_words(hundreds_digit) + "сотого")
            return f"{thousands_word} {hundreds_word}"
    else:
        thousands = n // 1000
        remainder = n % 1000
        if thousands == 1:
            thousands_words = "тысяча"
        elif thousands == 2:
            thousands_words = "две тысячи"
        elif thousands == 3:
            thousands_words = "три тысячи"
        elif thousands == 4:
            thousands_words = "четыре тысячи"
        else:
            thousands_words = number_to_words(thousands) + " тысяч"

        if remainder == 0:
            return thousands_words
        else:
            remainder_words = number_to_words(remainder)
            return thousands_words + " " + remainder_words

if __name__ == "__main__":
    date_input = input("Введите дату в формате ДД.MM.ГГГГ: ")
    try:
        day_str, month_str, year_str = date_input.strip().split('.')
        day = int(day_str)
        month = int(month_str)
        year = int(year_str)
    except ValueError:
        print("Неверный формат даты. Используйте ДД.MM.ГГГГ")
        exit()
    day_word = date_to_word(day)
    month_word = month_to_word(month)
    year_word = year_to_word(year)
    print(f"{day_word} {month_word} {year_word} года")
