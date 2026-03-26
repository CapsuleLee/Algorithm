import sys
import bisect

input = sys.stdin.readline

n, m =map(int,input().split())
result = dict()
temp = []
for i in range(n):
    title, num = map(str, input().split())
    result[i] = title
    temp.append(int(num))
for _ in range(m):
    x = int(input())
    idx = bisect.bisect_left(temp,x)
    print(result[idx])
