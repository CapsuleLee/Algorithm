t=int(input())

for testcase in range(1,t+1):

    n,k = map(int,input().split())
    candy = list(map(int,input().split()))

    candy.sort()
    result = 0
    answer = float('INF')
    for i in range(n-k+1):
        result = max(candy[i:i+k]) - min(candy[i:i+k])
        if answer > result:
            answer = result


    print(F"#{testcase}",answer)