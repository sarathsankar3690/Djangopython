pattern="ABBA"
flg=0
for char in pattern:
    if pattern.count(char)>1:
        flg=1
        print(char)
        break


# word="ABBA"
# for char in word:
#     if word.count(char)>1:
#         print(char)

