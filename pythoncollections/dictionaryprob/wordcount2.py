letters="ABBC"
dict={}
for letter in letters:
    if letter not in dict:
        dict[letter]=1
    else:
        print(letter, "is first")
        break


