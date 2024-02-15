def isEmpty(que):
    if(que==[]):
        return True
    else:
        return False

def Enqueue(que,item):
    que.append(item)
    if(len(que)==1):
        front=rear=0
    else:
        rear=len(que)-1

def Dequeue(que):
    if isEmpty(que):
        print("underflow")
    else:
        que.pop(0)
    if len(que)==0:
        front=rear=None

def peek(que):
    if isEmpty(que):
        print("underflow")
    else:
        front=0
    return que[front]
























