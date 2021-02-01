num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
num3=int(input("Enter the third number"))
if (num1>num2)&(num1>num3):
    print(num1,"is greatest among 3 numbers")
elif (num2>num1) & (num2>num3):
    print(num2,"is greatest among three numbers")
elif (num3>num1)&(num3>num2):
    print(num3,"is greatest among the three numbers")
elif (num1==num2) & (num1==num3):
    print("three numbers are equal")

