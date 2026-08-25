unit=int(input("Enter your unit:"))
connection_type=input("Enter your connection Type commercial/non-commercial:")
conn=connection_type.strip().lower()
if conn == "non-commercial":
    if unit<=200:
        print("Free")
    elif 200<= unit <=500:
        print("Total bill:",(unit-200)*4)
    elif 501<= unit <=2000:
        print("Total bill:",(unit-200)*8)
    else:
        print("Total Bill:",(unit-200)*10)
        
elif conn=="commercial":
    if unit<=500:
        print("Total bill:",unit*6)
    elif 501 <= unit <=1000:
        print("Total bill:",unit*9)
    elif 1001 <= unit <= 5000:
        print("Total bill:",unit*12)
    elif unit<=5000:
        print("Total bill:",unit*15)
else:
    print("Invalid connection type")


