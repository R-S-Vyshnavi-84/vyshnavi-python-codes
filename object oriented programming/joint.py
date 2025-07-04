
input_string = input("Enter a string: ")
uppercase_count = 0
lowercase_count = 0
digit_count = 0
special_symbol_count = 0

for char in input_string:
    if 'A' <= char <= 'Z':
        uppercase_count += 1
    elif 'a' <= char <= 'z':
        lowercase_count += 1
    elif '0' <= char <= '9':
        digit_count += 1
    else:
        special_symbol_count += 1

print("Uppercase characters:", uppercase_count)
print("Lowercase characters:", lowercase_count)
print("Digits:", digit_count)
print("Special symbols:", special_symbol_count)