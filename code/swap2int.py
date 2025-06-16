num1=10
num2=12
print(f"num1 = {num1}")
print(f"num2 = {num2}")
#python method
#num1,num2=num2,num1

temp=num1
num1=num2
num2=temp

print("after swappinng :")
num1=num1+num2
num2=num1-num2
num1=num1-num2
print(f"num1 = {num1}")