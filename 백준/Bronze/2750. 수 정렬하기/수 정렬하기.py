import sys

input = sys.stdin.readline

n= int(input())
ary=[]

for i in range(n):
    x=int(input())
    ary.append(x)
ary.sort()
for i in ary:
    print(i)