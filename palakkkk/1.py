# a="Palak Joshi"
# z=a.isspace()
# z=a.isnumeric()
# z=a.isalpha()
# z=a.isalnum()
# z=a.isupper()
# z=a.islower()
# z=a.istitle()
# z=a.isdigit()
# print(z)




line=input("Enter a line: ")
dc=0
ac=0
for i in line:
    if i.isdigit():
        dc+=1
    elif i.isalpha():
        ac+=1
print("Number of digits: ",dc)
print("Number of alphabets: ",ac)


a="My name is Palak"
# for i in a:
#     print(i)

for i in range(len(a)):
    print(a[i])











