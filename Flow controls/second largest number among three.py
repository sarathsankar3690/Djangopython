num1=int(input("Enter the first number"))
num2= int(input("Enter the second number"))
num3= int(input("Enter the third number"))
if (num1>num2)&(num1>num3):
    if (num2>num3):
        print(num2,"is the second largest number")
    else:
        print(num3,"is second largest number")
elif (num2>num1)&(num2>num3):
    if (num1>num3):
        print(num1,"is the second largest number")
    else:
        print(num3,"is the second largest number")
elif (num3>num1)&(num3>num2):
    if(num1>num2):
        print(num1,"is the second largest number")
    else:
        print(num2,"is the second largest number")
