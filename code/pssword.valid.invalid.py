str=input("enter the pasword:")
alphabets=0
digits=0
special_characters=0
for ch in str:
    if ch.isalpha() and ch.isnumeric():
        if alphabets==0 and digits==0 and special_characters==0:
           print("!!password is invalid try another!!")
        else:
            print("!!valid!!")