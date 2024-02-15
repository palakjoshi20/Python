'''queue=["rahul", "harsh", "bobby", "palak"]
while(1):
    def enterElement():
        element=input ("enter the name:")
        queue.append((element))
        print (queue)
    def removeElement():
        popped=queue.pop(0)
        print(popped)
        print(queue)
    print("press 1 for adding the element\npress 2 for removal of elements")
    choice=int(input())
    if choice==1:
        enterElement ()
    elif choice==2:
        removeElement()
    else:
        break'''

'''s=input("Enter the string")
stack=[]
for i in s:
    stack.append(i)
for i in range(len(stack)-1,-1,-1):
    print(stack[i]*2,end=" ")'''

'''stack=[]
def push():
    element=input("enter the name: ")
    stack.insert(0,element)
    print(stack)
def pop():
    stack.pop()
    print(stack)
while(1):
    choice=input("Press Push or Pop: ")
    if choice=="Push":
        push()
    elif choice=="pop":
        pop()
    else:
        break'''

'''queue=[]
def push():
    element=input("enter the name: ")
    queue.append(element)
    print(queue)

i=0
def pop():
    queue[i]=None
    print(queue)

while(1):
    choice=input("Press Push or Pop: ")
    if choice=="push":
        push()
    elif choice=="pop":
        pop()
        i+=1
    else:
        print("Please enter a valid input")'''

'''queue=[]
def enque():
    element=input("enter the name: ")
    queue.append(element)
    print(queue)
def deque():
    choice=int(input("Press 1 for deque from first or press 2 for deque from last: "))
    if choice==1:
        queue.pop(0)
        print(queue)
    elif choice==2:
        queue.pop()
        print(queue)
while(1):
    c=int(input("Press 1 for enque and 2 for deque: "))
    if c==1:
        enque()
    elif c==2:
        deque()
    else:
        break'''

'''stack=[]
def push():
    city=input("Enter the city")
    pin=int(input("Enter the pincode: "))
    node=[city,pin]
    stack.append(node)
    print(stack)
def pop():
    stack.pop()
    print(stack)
    if len(stack)==0:
        print("the stack is empty no items can be popped")
while(1):
    c=int(input("Enter the choice: \n 1 for push \n 2 for pop:"))
    if c==1:
        push()
    elif c==2:
        pop()
    else:
        break'''

hpr=[]
lpr=[]
mpr=[]
def insert():
    element=input("Enter the name: ")
    priority=input("Enter the priority(h/m/l: ")
    if priority=="h":
        hpr.append(element)
    elif priority=="m":
        mpr.append(element)
    elif priority=="l":
        lpr.append(element)
    else:
        print("Enter a valid input(h/l/m)")
    print("hpr=", hpr)
    print("mpr=", mpr)
    print("lpr=", lpr)

def search():
    element=input("Enter the elememt: ")
    if element in hpr:
        print("The element is in highest priority")
    elif element in mpr:
        print("The element is in mid priority")
    elif element in lpr:
        print("The element is in lowest priority")
    else:
        print("The element is not present in any queue")

def change():
    element=input("Enter the element: ")
    priority=input("Enter the priority(I/D: ")
    if priority=='I':
        if element in hpr:
            print("Element is already in HIghest priority")
        elif element in mpr:
            hpr.append(element)
            mpr.remove(element)
        elif element in lpr:
            mpr.append(element)
            lpr.remove(element)
        else:
            print("Element is not present")
    elif priority=='D':
        if element in lpr:
            print("Element is already in lowest priority")
        elif element in mpr:
            lpr.append(element)
            mpr.remove(element)
        elif element in hpr:
            mpr.append(element)
            hpr.remove(element)
        else:
            print("Element is not present")
    print("hpr=", hpr)
    print("mpr=", mpr)
    print("lpr=", lpr)
while(1):
    A=int(input("Enter the choice:\n 1:Insert element\n 2:Search for elemnt\n 3:Change priority"))
    if A==1:
        insert()
    elif A==2:
        search()
    elif A==3:
        change()
    else:
        break





































































