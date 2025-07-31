import sys

input = sys.stdin.readline

t=int(input())
dp = [1,1,3,5]

for i in range(4,51):
    dp.append(((dp[i-1]-dp[i-2])+(dp[i-2]-dp[i-3])+dp[i-1])%1000000007)
print(dp[t])
