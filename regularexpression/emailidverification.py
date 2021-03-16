from re import*
rule="[a-zA-Z0-9]+{1,64}@gmail.com"
variable_name=input("Enter the email ID: ")
matcher=fullmatch(rule,variable_name)

if matcher!=None:
    print("Valid Email Id")
else:
    print("Invalid Email Id")