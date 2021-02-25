f=open("words","r")
lst=[]
dict={}
for w in f:
    words=w.rstrip("/n").split(" ")
    for wordss in words:
        lst.append(wordss)


# for wordss in lst:
#     print(wordss)
    # wrdset+=w.rstrip("/n").split(" ")
# print(wrdset)