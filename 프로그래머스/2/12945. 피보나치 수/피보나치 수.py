def solution(n):
    answer = 0
    dp = [0,1]
    for i in range(2,100001):
        dp.append(dp[i-2]+dp[i-1])
    answer = dp[n]%1234567
    return answer