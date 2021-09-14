import sys

n= int(sys.stdin.readline().rstrip())
lst=[]


def push(number):
   lst.append(number)

def pop():
    if len(lst)==0:
        return -1
    else :
        return lst.pop()

def size():
    return len(lst)

def empty():
    if len(lst)==0:
        return 1
    else :
        return 0

def top():
    if len(lst)==0:
        return -1
    else :
        return lst[-1]



for i in range(n):
    command= sys.stdin.readline().rstrip().split()
    string=command[0]                   #명령어
    if(string=="push"):
        push(int(command[1]))
    elif(string=="pop"):
        print(pop())
    elif(string=="size"):
        print(size())
    elif(string=="empty"):
        print(empty())
    elif(string=="top"):
        print(top())
