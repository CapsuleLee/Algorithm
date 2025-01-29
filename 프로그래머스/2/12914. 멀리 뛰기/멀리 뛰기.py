def solution(n):
    dp=[0,1,2]
    for i in range(3,2001):
        dp.append(dp[i-2]+dp[i-1])
    answer = dp[n]%1234567
    
    return answer