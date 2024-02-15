#function increases reusability
#void
'''def hello():
    print("hello world")
hello()'''
#non-void
"""def bobby():
    return "hello world"
print(bobby())"""
#a and b are parameters and their valuea are argument
"""def sum(a,b):
    print("the sum of a and b is",a+b)
a=int(input("enter the value of a: "))
b=int(input("enter the value of b: "))
sum(a,b)"""
#return will store values and we can use them later
"""def prahlad(a,b):
    return a+b
def bobby(a,b):
    return a*b
sum=prahlad(6,8)
product=bobby(3,4)
print(sum-product)"""
#simple interest
"""def SI(P,R,T):
    print("simple interest is",(P*R*T)/100)
SI(100,40,40)"""
#positional argument eg-(p,r)(3,4) so p gets 3 and r gets 4
#default argument eg-(p,t,r=10)(100,1) r gets value by default,(default values will always be kept at last)
#keyword arguments (p,t,r)(r=10,t=6,p=9) assign values to all

#LOCAL VARIABLE-1st priority
#family
#GLOBAL VARIABLE-2nd priority bahar k log

#Pattern
'''rows=int(input("enter the number of rows"))
for i in range(rows):
    for j in range(rows-i):
        print("*",end=" ")
    print()'''

# rows=int(input("enter the number of rows"))
# for i in range(rows):
#     for j in range(1+i):
#         print("*",end=" ")
#     print()

'''rows=int(input("enter the number of rows: "))
for i in range(1,rows+1):
    for j in range(rows-i+1):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()'''


'''sum=0
for i in range(1,11):
    sum+=i
print(sum)'''

"""num=int(input("enter the number"))
for i in range(1,num+1):
    print("the cube of",i,"is: ",i*i*i)
print()"""

'''num=int(input("enter the num: "))
oddsum=0
for i in range(1,num+1):
    if (num%2!=0):
        oddsum+=i
print(oddsum)'''

'''n = int(input("Enter the number : "))
oddsum = 0
for i in range(1, n+1):
  if i % 2 == 0:
    oddsum += 0
  else:
    oddsum +=i
print(oddsum)'''
#
# n = int(input("Enter the number : "))
# for i in range(n):
#   for j in range(i+1):
#     print(j+1,end=" ")
#   print("\n")

# n=int(input("enter the number: "))
# for i in range(n):
#   for j in range(n-i):
#     print(j+1,end=" ")
#   print()

'''n=3
if n%2!=0:
    print("Weird")
elif n%2==0 and (n>=2) and (n<=5):
    print("Not Weird")
elif n%2==0 and (n>=6) and (n<=20):
     print("Weird")
elif n%2==0 and (n>20):
    print("Not Weird")'''

'''l=[1,2,3]
m=[2,5,7]
n=[]
for i in range(3):
    val=l[i]+m[i]
    n.append(val)
print(n)'''




