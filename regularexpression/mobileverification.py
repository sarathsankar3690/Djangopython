from re import*
rule="[+]91\d{10}"
variable_name=input("Enter the number: ")
matcher=fullmatch(rule,variable_name)

if matcher!=None:
    print("Valid Indian mobile number")
else:
    print("Number not Valid in India")
