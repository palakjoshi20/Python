# def fun(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#         i+=1
#     return fact
# print(fun(5))
#

# def wish():
#     print("good mrng")
# wish()


# def fact(n):
#     if n==0:
#         return 1
#
#     return n*fact(n-1)
#
# print(fact(5))

def fibo(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)
fibo(6)



