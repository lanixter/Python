s = input(); print('+' + ''.join(filter(str.isdigit, s[1:]))) if s.startswith('+') else print(''.join(filter(str.isdigit, s)))
