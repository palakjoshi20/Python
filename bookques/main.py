'''a=0.2+9.4j
b=1.2+3.4j
c=a+b
print(c)'''


'''elements=[10,20,40,210,226]
x=bytes(elements)
for i in x:
    print(i)'''

'''p=int(input("enter a string"))
print(p)'''

'''a=eval('5+6')
print(a)'''

'''list=[]
n=int(input("enter the no of elements: "))
for i in range(n):
    k=input("enter the elements:")
    a=list.append(k)
print(list)'''

'''list=[]
n=int(input("enter the no of elements: "))
for i in range(n):
    k=input("enter the elements:")
    list.append(k)
p=tuple(list)
print(p)'''

'''a=int(input("enter the value of a: "))
c=a*a
print(c)'''

'''a=int(input("enter the number: "))
b=int(input("enter the power: "))
c=a**b
print(c)'''

'''r=int(input("Enter the radius: "))
area= 22/7 * r*r
print(area)'''

'''b=19
if b==19:
    print("the value is correct")
    print("its 19")'''

'''n=int(input("Enter the number: "))
if n%2==0:
    print("the number is even")
else:
    print("the number is odd")'''

'''n=int(input("Enter the number: "))
if (n>=1 and n<=10):
    print("the number is b/w 1 to 10")
else:
    print("the number is not")'''

'''n=int(input("Enter the number: "))
if n==0:
    print("the number is zero")
elif n>0:
    print("the number is positive")
elif n<0:
    print("the number is negative")'''

'''i=1
while i<=10:
    print(i)
    i+=1'''

'''for i in range(100,201):
    if i%2==0:
        print(i," is even")
    else:
        print(i," is odd")'''

'''m=int(input("enter the value of m: "))
n=int(input("enter the value of n: "))
for i in range(m,n+1):
    if i % 2 == 0:
        print(i, " is even")'''

'''str='palakjoshi'
for i in str:
    print(i)'''

'''str="palak joshi"
n=len(str)
for i in range(n):
    print(str[i])'''

'''for i in range(1,11):
    if i%2!=0:
        print(i)'''

'''i=10
while i>=1:
    print(i)
    i-=1'''

'''list=["palak","o","7"]
for i in list:
    print(i)'''

'''list=[1,4,5,6,7]
sum=0
for i in list:
    print(i)
    sum+=i
print("sum is ",sum)'''

'''list=[1,4,5,6,7]
sum=0
i=0
while i<len(list):
    print(list[i])
    sum+=list[i]
    i+=1
print(sum)'''

'''n=int(input("Enter the number of rows:"))
for i in range(n+1):
    for j in range(1,i+1):
        print("* ",end="")
    print()'''

'''winner={}
n=int(input("Enter the num of data: "))
for i in range(n):
    key=input("enter the country: ")
    value=int(input("Enter no of medals: "))
    winner[key]=value
print(winner)'''

'''str="palakjoshi"
count=0
for i in str:
    count+=1
print(count)'''

'''list=["palak","bobby","harsh","rahul"]
list.insert(3,"kiki")
print(list)'''

'''str="this python programming"
add=input("enter the substring: ")
n=int(input("enter the position you want to insert the substring: "))
str1=[]
for i in range(len(str)):
    str1.append(str[i])
str1.insert(n," "+add)
hey="".join(str1)
print(hey)'''

# def leapyear(y):
#
#     if (y%4==0 and y%100!=0 or y%400==0):
#         print("its a leap year")
#     else:
#         print("its not a leap year")
#
# leapyear(1900)
'''n= int(input("How many terms the user wants to print? "))

# First two terms
n1 = 0
n2 = 1
count = 0

# Now, we will check if the number of terms is valid or not
if n <= 0:
    print("Please enter a positive integer, the given number is not valid")
# if there is only one term, it will return n_1
elif n == 1:
    print("The Fibonacci sequence of the numbers up to", n, ": ")
    print(n1)

else:
    print("The fibonacci sequence of the numbers is:")
    while count < n:
        print(n1)
        nth = n1 + n2
        # At last, we will update values
        n1 = n2
        n2 = nth
        count += 1'''






























