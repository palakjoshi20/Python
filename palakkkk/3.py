# import math
# print(math.sqrt(16))
# print(math.ceil(1.3))
# print(math.floor(1.3))
# print(math.pow(2,4))

#Conditional Statements
# num=int(input("Enter a number: "))
# if num>0:
#     print(num," is positive")
# else:
#     print("number is negative")

'''grade=input("Enter your grade")
if grade=="A":
    print("You passed the exam")
else:
    print("You failed")'''

'''grade=input("Enter your grade")
if grade=="A":
    print("you are first")
elif grade=="B":
    print("you are second")
elif grade=="C":
    print("You are third")
else:
    print("you failed")'''

'''runs=int(input("Enter the runs: "))
if runs>=100:
    print("You scored a century")
elif runs>=50:
    print("You scored half century")
else:
    print("Neither a century nor a 50")'''
#
# a=int(input("Enter the first number: "))
# b=int(input("Enter the second number: "))
# c=int(input("Enter the third number: "))
# max=a
# if b>max:
#     max=b
# if c>max:
#     max=c
# print("largest is",max)

'''num=int(input("Enter a number between 0-999: "))
if num==0:
    print("You've entered 0")
elif num<10:
    print("1 digit number")
elif num<100:
    print("2 digit number")
elif num<1000:
    print("3 digit number")
else:
    print("number is not in the range of 0-999")'''

# h=float(input("Enter your height in metres: "))
# w=float(input("Enter your weight in kg: "))
# BMI=w/(h**2)
# if BMI<18.5:
#     print("Your BMI is",BMI,".You are underweight")
# elif BMI>=18.5 and BMI<=24.9:
#     print("Your BMI is",BMI,"You're healthy")
# elif BMI>24.9 and BMI<=29.9:
#     print("Your BMI is",BMI,"You're overweight")
# else:
#     print("Your BMI is",BMI,"Obese")


'''r=float(input("Enter the radius: "))
choice=int(input("Enter the choice 1 or 2: "))
if choice==1:
    print("Circumference is:",2*3.14*r)
elif choice==2:
    print("area is",3.14*r*r)
else:
    print("Enter valid choice")'''

# x=int(input("Enter a number: "))
# y=int(input("Enter a number: "))
# z=int(input("Enter a number: "))
#
# max=mid=min=None
#
# if x<y and x<z:
#     if y<z:
#         max,mid,min=z,y,x
#     elif z<y:
#         max,mid,min=y,z,x
# elif y<x and y<z:
#     if x<z:
#         max,mid,min =z,x,y
#     elif z<x:
#         max,mid,min =x,z,y
# else:
#     if x<y:
#         max,mid,min=y,x,z
#     elif y<x:
#         max,mid,min=x,y,z
#
# print("Numbers in ascending order: ",min,mid,max)
# print("Numbers in descending order: ",max,mid,min)

'''for i in range(15,21):
    print("Cube of",i,"is ",i**3)'''

# sum=0
# for i in range(1,8):
#     sum+=i
#     print(sum)

'''sum=0
for i in range(1,20):
    if i%2!=0:
        sum+=i
print(sum)'''

'''palak=[1,2,3,4,5]
for i in palak:
    print(i)'''

'''num=97586546
n=str(num)
count=0
for i in n:
    count+=1
print(count)'''

'''li=[1,2,3,4,5,6,7,8,9,10]
for i in li:
    if i%2==0:
        print(i," is even")
    else:
        print(i," is odd")'''

'''num=5
fact=1
for i in range(1,6):
    fact=fact*i
print(fact)'''

'''a=" is a student"
if "neha" in a:
    print("neha is there")
else:
    print("neha is not there")'''

'''a=" Hello! World "
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("H","Y"))
print(a.split("o"))
print("5"+"World")
print(a+"this"+"2")'''

# b=4
# age=12
# a="My age is {},{}"
# print(a.format(age,b))

'''a="My name is riya,my hobby is sleeping"

print(a.capitalize())
print(a.casefold())
print(a.count("is"))
print(a.endswith("."))
print(a.find("riya"))
print(a.index("riya"))

b="SUMAn"
print(b.isalnum())
print(b.isalpha())
print(b.islower())
print(b.isdigit())
print(b.isidentifier())
print(b.isdecimal())
print(b.isnumeric())
print(b.isspace())
print(b.istitle())
print(b.isupper())'''

# print(bool())



















