dp = [0,1]

for i in range(2,10002):
    dp.append(dp[i-2]+dp[i-1])

t=int(input())

for i in range(1,t+1):
    p,q = map(int,input().split())
    print("Case #%d: %d"%(i,dp[p]%q))
