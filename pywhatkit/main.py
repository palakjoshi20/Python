import pywhatkit as py
list=["+919456733415"]
h=10
m=1
for i in range(len(list)):
    py.sendwhatmsg(list[i],"Hello",h,m)
    m+=1


