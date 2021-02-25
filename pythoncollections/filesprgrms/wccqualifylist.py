f1=open("teams","r")
f2=open("drop","r")
# teamset=set()
# dropset=set()
# for lines in f1:
#     teamset.add(lines.rstrip("\n"))
# for li in f2:
#     dropset.add(li.rstrip("\n"))
# qualset=teamset.difference(dropset)
# print(qualset)
def get_team_set(f):
    st=set()
    for lines in f:
        st.add(lines.rstrip("\n"))
    return st
teamset=get_team_set(f1)
dropset=get_team_set(f2)
qual=teamset-dropset
print(qual)