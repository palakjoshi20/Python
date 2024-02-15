#File Handling//we store output
f=open("text.txt","r")
str=f.read(5)#read reads text one  by one
print(str)



'''f=open("text.txt","r")
str=" "
count=1
vcount=0
ccount=0
while str:
    str=f.read(1)
    if str.isspace():
        count+=1
    elif str in ["a","e","i","o","u","A","E","I","O","U"]:
        vcount+=1
    else:
        ccount+=1
print(count)
print(vcount)
print(ccount)'''

'''f=open("text.txt","r")
str=" "
while str:
    str=f.readline()
    print(str,end="")'''

'''f=open("text.txt","r")
str=" "
str=f.readline()
print(str,end="")'''

'''f=open("text.txt","r")
str=" "
str=f.readlines()
print(str,end="")'''

# f=open("bobby.txt","w")
# for i in range(5):
#     name=input("Enter the name: ")
#     f.write(name+"\n")

#append mode adds to the previous data without overwriting
'''f=open("bobby.txt","a")
list=[]
for i in range(5):
    name=input("Enter the name: ")
    list.append(name+"\n")
f.writelines(list)
f.close()'''

# f=open("bobby.txt","a")
# list=[]
# for i in range(2):
#     name=input("Enter the name: ")
#     rollno=int(input("enter the rollno: "))
#     marks=float(input("enter the marks: "))
#     list.append("roll no "+ str(rollno) + " with name " +name+ " has got " +str(marks)+ " marks " +"\n")
# f.writelines(list)

# f=open("text.txt","w")





















