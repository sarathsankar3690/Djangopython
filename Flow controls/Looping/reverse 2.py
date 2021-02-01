num=int(input("enter the number"))

while (num!=0): #123!=0 12!=0 1!=0 0!=0
    digit=num%10 #digit=3 digit=12%10=2 1%10=1
    print(digit, end="")
    num=num//10 #123//10=12 12//10=1 1//10
