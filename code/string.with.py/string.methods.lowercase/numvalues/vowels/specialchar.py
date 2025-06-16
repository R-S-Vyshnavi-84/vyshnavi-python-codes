input_str=input("enter the string:")
digit_count=0
vowel_count=0
specialchar=0
for ch in input_str.lower():
    if ch.isdigit():
        digit_count+=1
    elif ch.isalpha():
        if ch in ['a','e','i','o','u']:
            vowel_count+=1
    else:
        specialchar+=1
print(f"digit count: {digit_count}")
print(f"vowel count: {vowel_count}")
print(f"special char: {specialchar}")