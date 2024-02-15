'''dob=int(input("year of birth: "))
currentyear=int(input("enter year: "))
age=currentyear-dob
print("you will  be",age,"in",currentyear)'''

'''list=[2,3,4,5,6,4,3]
li=[]
for i in range (len(list)):
    for j in range(i,len(list)):
        if list[i]!=list[j]:
            li.append(list[i])
            break
print(li)'''

'''list=["bobbyy","palak","harshwardhan","rahul","ashu"]
longest=list[0]
for i in range(len(list)):
    if len(longest)<len(list[i]):
        longest = list[i]
print(longest)'''

'''list1=[2,4,6]
list2=[5,7,9]
list=[]
for i in range (len(list1)):
 
        a=list1[i]+list2[i]
        list.append(a)
   
print(list)'''

'''def sum(a,b):
    c=a+b
    print("sum=",c)
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
sum(6,7)'''

def sum(a,b):
   c=a+b
   return c
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
print(sum(a,b))














