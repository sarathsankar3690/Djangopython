text="hello hai hello hai yard hello yeah an"
words=text.split(" ")
dict={}
# for word in words:
#     if word not in dict:
#         dict[word]=1
#     else:
#         dict[word]+=1
for word in words:
    if word not in dict:
        dict[word]=1
    else:
        dict[word]+=1
print(dict)
print(sorted(dict, key=dict.get, reverse=True))



