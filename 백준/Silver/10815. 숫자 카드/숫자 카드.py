import sys

n=int(sys.stdin.readline())
cardNum=set(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
check=list(map(int,sys.stdin.readline().split()))

for i in check:
    if i in cardNum:
        print("1",end=" ")
    else:
        print("0",end=" ")
