# def wish():
#     print("good morning")
# wish()

# def sum(a,c,b=10):
#     return a+b+c
# print(sum(2,3,4))


#Built-in function==len(),int(),input()
#Module functions==import math
#user-defined

# def cube(a=2):
#     print(a**3)
# n=input("Enter a num: ")
# if n=="":
#     cube()
# else:
#     cube(int(n))


# def sum(a,b):
#     return a+b
# def diff(a,b):
#     return a-b
# def pro(a,b):
#     return a*b
# def div(a,b):
#     return a/b
# print("Press 1 for addition\nPress 2 for sub\nPress 3 for multi\nPress 4 for div")
# choice=int(input("Enter your choice: "))
# a=int(input("enter a: "))
# b=int(input("enter a: "))
# if choice==1:
#     print(sum(a,b))
# elif choice==2:
#     print(diff(a,b))
# elif choice==3:
#     print(pro(a,b))
# elif choice==4:
#     print(div(a,b))


# def fun():
#     return None
# print(fun())


# def one(a):
#     return a%10
# print(one(234))
#


#
# def fun(n):
#     count = 0
#     for i in range(1, n + 1):
#         if n % i == 0:
#             count += 1
#     if count == 2:
#         print("num is prime")
#     else:
#         print("not prime")
# n=int(input("Enter the value of n: "))
# fun(n)


# def one(N,M):
#     n=N%10
#     m=M%10
#     if (n>m):
#         return M
#     else:
#         return N
# print(one(23421,5617))


# def nthroot(x,n=2):
#     return x**(1/n)
# print(nthroot(4,2))


# n=int(input("Enter the num of rows: "))
# for i in range(0,n):
#     for j in range(0,i+1):
#         print("* ",end="")
#     print("")


# def li(list):
#     sum=0
#     for i in list:
#         sum+=i
#     print(sum)
# list=[1,2,3,4]
# li(list)

# def fun(li):
#     li2=[]
#     for i in li:
#         if i%2==0:
#             li2.append(i)
#     return li2
# list=[1,2,3,4,5,6,7,8]
# print(fun(list))

# def fun(li):
#     li2=[]
#     for i in li:
#         if i not in li2:
#             li2.append(i)
#     return li2
# list=[2,2,3,3,4,5,6,4]
# print(fun(list))

# def BMI(w,h):
#     BMI=w/(h**2)
#     if BMI<18.5:
#         print("Your BMI is",BMI,".You are underweight")
#     elif BMI>=18.5 and BMI<=24.9:
#         print("Your BMI is",BMI,"You're healthy")
#     elif BMI>24.9 and BMI<=29.9:
#         print("Your BMI is",BMI,"You're overweight")
#     else:
#         print("Your BMI is",BMI,"Obese")
# BMI(42,1.5)

# def palin(num):
#     temp=num
#     rev=0
#     while(num>0):
#         rev=rev*10+num%10
#         num=num//10
#     if temp==rev:
#         print(temp," is palindrome")
#     else:
#         print(temp," is not palindrome")
# palin(525)


# def fun(str1,str2):
#     a=len(str1)
#     b=len(str2)
































str="My name, is Palak ."
def fun(str):
    for i in str:
        if i.isalpha():
            continue
        if i.isspace():
            continue
        else:
            print(i)
fun(str)











































