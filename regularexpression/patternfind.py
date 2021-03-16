# from re import *
# pattern="ab"
#
# source="abababbbab"
# matcher=finditer(pattern,source)
# cnt=0
# for match in matcher:
#     print(match.start())
#     print(match.group())
#     cnt+=1
# print(cnt)

from re import *

# pattern='[abc]'
# pattern='[a-z]'
# pattern='[A-Z]'
# pattern='[^0-9]'
# pattern='[\W\d]'
# source="ab Zk@9c"
# matcher=finditer(pattern,source)
# for match in matcher:
#     print(match.start())
#     print(match.group())


# pattern="a+" #checking consecutive 'a's
# source="aaacaaabaaad"
# matcher=finditer(pattern,source)
# for match in matcher:
#     print(match.start())
#     print(match.group())


# pattern="a*" #a+ +zero number of a
# pattern="a{2}" #only two a's are counted
# pattern="a{2,3}"
source="aaacaaabaaad"
matcher=finditer(pattern,source)
for match in matcher:
    print(match.start())
    print(match.group())



