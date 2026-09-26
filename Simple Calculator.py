num1=int(input("Number1:"))
operation=input("Enter operation:")
num2=int(input("Number2:"))
if operation=="+":
    print("Add:",num1+num2)
elif operation=="-":
    print("Substract:",num1-num2)
elif operation=="*":
    print("Multiple:",num1*num2)
elif operation=="/":
    print("Division:",num1/num2)
elif operation=="%":
    print("Modules:",num1%num2)
elif operation=="//":
    print("Floor div:",num1//num2)
else:
    print("Invalid operation")