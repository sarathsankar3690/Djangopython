employees=[
    {"names":"varun","desig":"develop","salary":40000,"join":2000,"resign":2008},
    {"names":"ram","desig":"develop","salary":30000,"join":1989,"resign":1995},
    {"names":"raju","desig":"qa","salary":28000,"join":2004,"resign":2010},
    {"names":"ravi","desig":"qa","salary":32000,"join":2005,"resign":2015},
    {"names":"sravan","desig":"mrkt","salary":35000,"join":2010,"resign":2020},
]

maxsal=max(list(map(lambda emp:emp["salary"],employees)))
print(maxsal)

hiem=list(filter(lambda emp:emp["salary"]==maxsal,employees))
print(hiem)

exp=list(filter(lambda emp:emp["resign"]-emp["join"]>8,employees))
print(exp)
