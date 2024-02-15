'''def checknum(n):
    if n%2==0:
        print("no is even")
    else:
        print("no is odd")

n=int(input("enter the number: "))
checknum(n)'''

'''def primenum(n):
    for i in range(1,n+1):
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
        if count==2:
            print("the number is prime")
        else:
            print("the number is composite")
primenum(7)'''

#1
'''def d2rn(d):
    return 82*d
def d2rv(d):
    print("in rupees",82*d)
d = int(input("enter in dollars"))
d2rv(d)
print(d2rn(d))'''

#2
'''def volume(l,b,h):
    return l*b*h
l=float(input("enter the length: "))
b=float(input("enter the breadth: "))
h=float(input("enter the height: "))
print("the volume is",volume(l,b,h))'''

#3
'''def cube(n=2):
    print(n*n*n)
    (2, int(num/2)+1)
cube()'''

'''num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

else:
    print(num, "is not a prime number")'''



'''import random
def num(a,b):
    print(random.randint(a,b))
a=int(input("Enter the number: " ))
b=int(input("Enter the number: " ))
num(a,b)'''

#5
'''a=input("Enter the first string: ")
b=input("Enter the second string: ")
def num(a,b):
    return
if len(a)==len(b):
            print("true")
else:
            print("False")

num(a,b)'''

#6
'''def nthroot(x,n):
    return
x=int(input("enter x: "))
n=int(input("enter n: "))
if n==0:
    print(x**1/2)
else:
    print(x**1/n)
nthroot(x,n)'''

#7


'''num=int(input("enter the number"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print()'''



'''list=["Palak","Aditya","Kartik","Bobby"]
while True:
    choice=int(input("Enter your choice \nPress 1 for insertion \nPress 2 for deletion \nPress 3 for first element \nPress 4 for exit: "))
    if choice==1:
        Element=input("Enter the element: ")
        list.append(Element)
        print(list)
    elif choice==2:
        if len(list)==0: print("Underflow")
        else: list.pop(0)
        print(list)
    elif choice==3:
        print(list[0])
    else:
        break'''

'''def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))'''

#sortinglist
"""list=[5,1,2,6,4,3,7]
for i in range(len(list)):
    for j in range(len(list)):
        if list[i]<list[j]:
            c=list[i]
            list[i]=list[j]
            list[j]=c
print(list)"""

#ask user
'''list=[]
no=int(input("enter the number you want to insert in the list: "))
for i in range(no):
    val=int(input("Enter the no: "))
    list.append(val)
for i in range(len(list)):
    for j in range(len(list)):
        if list[i]<list[j]:
            c=list[i]
            list[i]=list[j]
            list[j]=c
print(list)'''

'''list=["palak","bobby","kiki","mannu"]
req_list=sorted(list)
print(sorted(list))'''


'''list=[5,1,2,6,4,3,7,13]
for i in range(len(list)):
    for j in range(len(list)):
        if list[i]<list[j]:
            c=list[i]
            list[i]=list[j]
            list[j]=c
print(list)
new=int(input("enter the new element"))
list.append(new)
print(sorted(list))'''

'''list=[]
no=int(input("enter the number you want to insert in the list: "))
for i in range(no):
    val=input("Enter the no: ")
    list.append(val)
for i in range(len(list)):
    for j in range(len(list)):
        if list[i]<list[j]:
            c=list[i]
            list[i]=list[j]
            list[j]=c
print(list)'''

'''list=[]
no=int(input("enter the number of names you want to insert in the list: "))
for i in range(no):
    val=input("Enter the name: ")
    list.append(val)
for i in range(len(list)):
    for j in range(len(list)):
        if list[i]<list[j]:
            c=list[i]
            list[i]=list[j]
            list[j]=c
name=input("enter the name you want to insert: ")
for i in range(len(list)):
    if list[i]>name:
        list.append(name)
        break;
print(list)'''

'''list=[]
a=input("Enter the name: ")
for i in range(len(a)):
    list.append(a[i])
for i in range(len(list)):
    for j in range(len(list)):
        if list[i]<list[j]:
            c=list[i]
            list[i]=list[j]
            list[j]=c
print("".join(list))'''

'''num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

else:
    print(num, "is not a prime number")'''




def primenum(n):
    for i in range(1,n+1):
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
        if count==2:
            print(i,"the number is prime")

primenum(100)