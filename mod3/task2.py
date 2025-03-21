print((lambda n: f"{bin(n)[2:]}, {oct(n)[2:]}, {hex(n)[2:].upper()}" if n > 0 else "Неверный ввод")(int(input())))
