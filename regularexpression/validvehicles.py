from re import*
rule="KL[\d]{2}[A-Z]{2}[\d]{1,4}"
f=open("regnos","r")
lst=[]
for match in f:
    file1=match.rstrip("\n")
    matcher=fullmatch(rule,file1)
    if matcher!=None:
        lst.append(file1)
print(lst)


