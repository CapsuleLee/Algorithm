import sys 
input= sys.stdin.readline
x=int(input())
z=set()
for i in range(x):
    a=int(input())
    z.add(a)
z=sorted(z)
for i in z:
    print(i)

