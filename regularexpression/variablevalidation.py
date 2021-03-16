#first character must be from a-k
#second character must be a digit divisible by 3
#followed by any number of characters

from re import *
# rule="[a-kA-K][369][a-zA-Z0-9]*"
rule="[K][L][0-9]{2}[A-Z]{2}[0-9]{1,4}"
variablename=input("enter the variable name")

matcher=fullmatch(rule,variablename)
if matcher!=None:
    print("Valid variable")
else:
    print("Invalid variable")
