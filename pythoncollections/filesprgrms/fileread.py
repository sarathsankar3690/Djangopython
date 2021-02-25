f=open("demo","r")
lst=[]
for lines in f:
    lst.append(lines.rstrip("\n"))
ls=set(lst)
print(lst)

