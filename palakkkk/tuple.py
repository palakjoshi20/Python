#mytuple=("palak",9,"neha","priyanka",7,9,1)
# print(mytuple)
# print(len(mytuple))
# print(type(mytuple))
# print(mytuple[-5:-2])
# print(mytuple[3])
# if 19 not in mytuple:
#     print("yes")
# else:
#     print("No")
#
# x=list(mytuple)
#
# x[2]="nikhil"
# print\

# x=("nikhil",)
# mytuple += x
# print(mytuple)
#
# y=list(mytuple)
# y.remove(7)
# print(y)
#
# del mytuple
#print(mytuple)


# palak=("neha","suman","nikhil")
# (a,b,c)=palak
# print(a)
# print(b)
# print(c)

# palak=("neha","suman","nikhil","priyanka",7,9,1,7)
# (a,*b,c)=palak
# print(b)
# print(palak.count(7))
#print(palak.index(7))


tuple=('a','b','c','d')
char=input("enter the element you want: ")

if char in tuple:
    count = 0
    for i in tuple:
        if i!=char:
            count+=1
        else:
            break
    print(count)






















