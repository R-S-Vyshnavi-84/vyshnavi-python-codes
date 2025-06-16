str=input("enter the string:")
vowel_count_upper=0
vowel_count_lower=0
consonants_count=0
for ch in str:
    if str.isalpha():
        if ch in["a","e","i","o","u"]:
            vowel_count_lower+=1
        elif ch in ["A","E","I","O","U"]:
            vowel_count_upper+=1
        else:
            consonants_count+=1
print("vowel_count_lower",vowel_count_lower)
print("vowel_count_upper",vowel_count_upper)
print("consonants_count",consonants_count)
