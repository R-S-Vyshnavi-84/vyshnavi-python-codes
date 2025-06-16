num=int(input("enter a num:"))
if(num>=100 and num<=999 or num<=-100 and num>=-999):
    print("three digit number")
elif ((num>=1000 and num<=9999) or (num<=-1000 and num>=-9999)):
    print("four digit number")
else:
    print("not a three digit number")

