num=int(input("enter the month num:"))
if(num==1 or num==3 or num==5 or num==7 or num==8 or num==10 or num==12):
    print("number of days are 31")
elif(num==2):
    print("number of days are 28 or 29")
elif(num>12):
    print("invalid month number")
else:
    print("number of days are 30")