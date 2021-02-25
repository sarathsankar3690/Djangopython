f=open("covid_19_india(1).csv","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[3]
    confirm_cases=int(data[-1])
    cured_cases=int(data[-3])
    death_cases=int(data[-2])
    dict[state]={"state":state,"confirm":confirm_cases,"cured":cured_cases,"death":death_cases}
# for k,v in dict.items():
#     print(k,"===>",v)
#     break
print(dict)

