import sys

input = sys.stdin.readline

q=input().rstrip()
x=input().rstrip()
    
t=q.replace(x,".")
count=0

for i in t:
    if i == '.':
        count+=1
print(count)