# dd={"brand":"maruti","color":"grey","year":1993}
# print(dd)
# print(len(dd))
# print(dd["brand"])
aa=dict(name="suman", cc=11 , school="manas" )
# aa["rollno"]=21
# print(aa)
# print(aa.get("cc"))
# print(aa.keys())
# print(aa.values())
# print(aa.items())
# print(aa.popitem())
# del aa["cc"]
# aa["school"]="nbs"
# aa.update({"rollno":19})
# print(aa)
#
# for i in aa.items():
#     print(i)

#
# dd={"brand":"maruti","color":"grey","year":1993}
# a=input("enter the value: ")
# for i in dd:
#     if dd[i]==a:
#         print(i)


l1=[]
l2=[]
l3=[]
n=int(input("enter: "))
for i in range(n):
    a=int(input("enter: "))
    l1.append(a)
for i in range(n):
    a=int(input("enter: "))
    l2.append(a)
for i in range(n):
    a=(l1[i]+l2[i])
    l3.append(a)
print(l3)




































