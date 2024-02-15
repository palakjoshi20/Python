def isEmpty(stk):
    if(stk==[]):
        return True
    else:
        return False
def push(stk,item):
    stk.append(item)
    top=len(stk)-1

def spop(stk):
    if(isEmpty(stk)):
        return("Underflow")
    else:
        itemm= stk.pop()
        if(len(stk)==0):
            top=None
        else:
            top=len(stk)-1
    return itemm

def peek(stk):
    if isEmpty(stack):
        print("underflow")
    else:
        top=len(stk)-1
        return stk[top]

def display(stk):
    if isEmpty(stack):
        print("underflow")
    else:
        top=len(stk)-1
        print("top=",stk[top])
        for i in range(top-1,-1,-1):
            print(stk[i])
stack=[]
top = None
while True:
    print("1.Push")
    print("2.Pop")
    print("3.Peek")
    print("4.Display")
    print("5,Exit")
    ch=int(input("Enter a choice: "))
    if ch==1:
        item=input("Enter the item: ")
        push(stack,item)
    elif ch==2:
        item=spop(stack)
        if item=="Underflow":
            print("Stack is underflow")
        else:
            print(item," is the popped item")
    elif ch==3:
        item = peek(stack)
        if item=="Underflow":
            print("Stack is underflow")
        else:
            print(item, " is the top element")
    elif ch==4:
        display(stack)
    elif ch==5:
        break
    else:
        print("Invalid CHoice")






