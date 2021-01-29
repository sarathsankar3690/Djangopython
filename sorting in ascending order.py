num1=int(input("Enter the 1st number: "))
num2=int(input("Enter the 2nd number: "))
num3=int(input("Enter the 3rd number: "))
if (num1>num2)&(num1>num3):
    if(num2>num3):
        print(num3,num2,num1)
    else:
        print(num2,num3,num1)
if (num2>num1)&(num2>num3):
    if(num1>num3):
        print(num3,num1,num2)
    else:
        print(num1,num3,num2)
if (num3>num1)&(num3>num2):
    if(num1>num2):
        print(num2,num1,num3)
    else:
        print(num1,num2,num3)