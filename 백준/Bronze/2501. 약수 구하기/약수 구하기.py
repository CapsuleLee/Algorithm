import sys

input = sys.stdin.readline

n,k = map(int,input().split())
ary = set()

for i in range(1,int(n**0.5)+1):
    if n%i == 0:
        ary.add(i)
        ary.add(n//i)
result = sorted(ary)
try:
    print(result[k-1])
except:
    print(0)