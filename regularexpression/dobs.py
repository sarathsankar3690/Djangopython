from re import*
rule="[1-31][1-12]\d{4}"
f=open("dob","r")
lst=[]
for match in f:
    file1=match.rstrip("\n")
    matcher=fullmatch(rule,file1)
    if matcher!=None:
        lst.append(file1)
print(lst)