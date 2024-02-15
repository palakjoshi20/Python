def sort(li):
    temp=0
    for i in range(len(li)-1,0,-1):
        for j in range(i):
            if li[j]>li[j+1]:
                temp=li[j]
                li[j]=li[j+1]
                li[j+1]=temp
    print(li)
li=[5,3,6,8,1,9]
sort(li)