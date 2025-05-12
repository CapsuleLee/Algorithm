import sys

n=int(sys.stdin.readline().rstrip())

inputList=list(map(int,sys.stdin.readline().rstrip().split()))
stack=[]

num=1
for i in range(n):
    if inputList[0] != num:
        stack.append(inputList[0])
        inputList.pop(0)
    else:
        inputList.pop(0)
        num+=1
    while stack and stack[-1] == num:
        stack.pop()
        num+=1

if not stack:
    print("Nice")
else:
    print("Sad")