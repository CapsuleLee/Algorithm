from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n, m = map(int,input().split())
    a = (list(map(int,input().split())))
    a.sort()
    a = deque(a)
    count = 0
    while a:
        if len(a) >1 and a[0] + a[-1] <= m:
            a.popleft()
            a.pop()
            count += 1
        else:
            a.pop()
            count += 1
    print(f'Case #{i+1}: {count}')