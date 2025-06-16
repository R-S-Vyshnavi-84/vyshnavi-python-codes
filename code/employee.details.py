Employee={}
def Print_Emp():
    if bool(Employee):
        print("Here's the list of Employee...!")
        print(Employee)
    else:
        print("List is Empty")
def Add_Emp():
    Name=input("Enter the Full Name as per Aadhar :")
    ID=input("Enter the Employee ID: ")
    DOJ=input("Enter the Date of Joining in DD-MM-YYYY Format : ")
    Job=input("Enter the Designation : ")
    Dept=input("Enter Department : ")
    Sal=float(input("Enter the Salary : "))
    Probation_status=input("Enter 'Yes' if Serving Probation Period else 'No': ")
    mode=input("Enter the mode of work assigned(WHH/WFO): ")
    Notice_period=input("Enter 'Yes' if Serving Notice Period else 'No' : ")
    Emp=[Name,ID,DOJ,Job,Dept,Sal,Probation_status,mode,Notice_period]
    Employee[ID]=Emp
    print("Employee Added....!")
def Remove_Emp():
    ID=input("Enter the ID of the Employee : ")
    del Employee[ID]
    print("Employee Removed....!")

def Verify_Background():
    ID=input("Enter the ID of employee whom you have to verify: ")
    Verify=input(f"Enter Yes if Background verification is completed for emp with ID {ID} else 'No': ")
    if Verify in "Yes yes":
        print("Verification is Completed")
    else:
        print("Verification is Pending!!!!!!!!!")
    

while(True):
    print("Choose the option Based on Your Requirement :")
    print("1.Print Current List of Employee")
    print("2.Add New Employee List of Employee")
    print("3.Remove a employee from List of Employee")
    print("4.Check for Background Verification")
    print("5.Print Finalized List of Employee")
    print("6.Exit")
    choice=int(input("Enter your choice: "))
    if(choice>=1 and choice<=6):
        if choice==1:
            Print_Emp()
        elif choice==2:
            Add_Emp()
        elif choice==3:
            Remove_Emp()
        elif choice==4:
            Verify_Background()
        elif choice==5:
            Print_Emp()
        else:
            print("Happy to see You...!Bye")
            break