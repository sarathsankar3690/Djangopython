employees=[
    [100,"Jack","developer",25000],
    [101,"john","developer",18000],
    [103,"jinu","tester",28000],
    [104,"dinu","manager",30000]

]
# for employee in employees:
#     print(employee[1])
# for job in employees:
#     if job[2]=="developer":
#         print(job)
# total=0
# for salary in employees:
#     total+=salary[3]
# print(total)
# sum=0
# for salary in employees:
#     if salary[3]>sum:
#         sum=salary[3]
# print(sum)

# highsal=0
# for emp in employees:
#     emp[3]>highsal
#     highsal=emp[3]
# print("high:=",highsal)
#
# sallist=[]
# for emp in employees:
#     sallist.append(emp[3])
# print("highest salary: ",max(sallist))

lst=[
    [10,20,30],
    [10,20,30],
    [50,60,70]
]
new_list=[]
for o in lst:
    for i in o:
        new_list.append(i)
print(new_list)
