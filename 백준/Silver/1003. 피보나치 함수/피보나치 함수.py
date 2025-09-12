import sys

input = sys.stdin.readline

n= int(input())

dp = [(1,0),(0,1),(1,1)]

for i in range(3,41):
    dp.append((dp[i-2][0]+dp[i-1][0],dp[i-2][1]+dp[i-1][1]))

for _ in range(n):
    num = int(input())
    print(*dp[num])