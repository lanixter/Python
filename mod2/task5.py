input_domain = input().strip()
domain_parts = []
current_part = ''
for char in input_domain:
    if char == '.':
        domain_parts.append(current_part)
        current_part = ''
    else:
        current_part += char
domain_parts.append(current_part)
for part in reversed(domain_parts):
    print(part)
