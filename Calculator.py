#Program to make calculator
##Driver Loop
again = "Y"
while (again == "Y"):
    ##Print options
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    choice = int(input("Pick an option (1/2/3/4):"))
    ##Addition
    if (choice == 1):
        num1=float(input("enter first number:"))
        num2=float(input("enter second number:"))   
        ans=(num1+num2)
        print(ans)
    ##Subtraction
    elif (choice == 2):
        num1=float(input("enter first number:"))
        num2=float(input("enter second number:"))
        ans=(num1-num2)
        print(ans)
    ##Multiplication
    elif (choice == 3):
        num1=float(input("enter first number:"))
        num2=float(input("enter second number:"))
        ans=(num1*num2)
        print(ans)
    ##Division
    elif (choice == 4):
        num1=float(input("enter first number:"))
        num2=float(input("enter second number:"))
        ans=(num1/num2)
        print(ans)
    ##Driverloop question
    again = input("Enter Y to continue or any other key to stop: ").upper()
