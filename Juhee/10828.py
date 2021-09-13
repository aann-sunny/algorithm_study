import sys
num = int(input())
stack=[]

for i in range (num):
    command = list(map(str,sys.stdin.readline().split()))
    if command[0]=='push':
        stack.append(command[1])
    if command[0]=="top":
        if not stack:
            print(-1)
        else:
            print(stack[len(stack)-1])
    if command[0]=="size":
        print(len(stack))
    if command[0]=="empty":
        if not stack:
            print(1)
        else:
            print(0)
    if command[0]=="pop":
        if not stack:
            print(-1)
        else:
            top=stack.pop()
            print(top)
        
