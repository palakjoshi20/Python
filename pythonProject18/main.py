'''mat1=[[],[],[]]
mat2=[[],[],[]]
c=[[],[],[]]
for i in range(3):
    for j in range(3):
        a=int(input("Enter the no: "))
        mat1[i].append(a)
for i in range(3):
    for j in range(3):
        b=int(input("Enter the no: "))
        mat2[i].append(b)
for i in range(3):
    for j in range(3):
        s=mat1[i][j]+mat2[i][j]
        c[i].append(s)
print(c)'''

dict={"a":1,"b":2,"c":3}
'''x=dict.get("a")
y=dict.get("b")
z=dict.get("c")
print(x+y+z)'''
x=dict.values()
sum=0
for i in x:
    sum+=i
print(sum)


























