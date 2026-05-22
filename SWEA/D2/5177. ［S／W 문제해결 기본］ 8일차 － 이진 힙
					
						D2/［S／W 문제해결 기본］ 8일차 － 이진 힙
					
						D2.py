import heapq

t = int(input())

for testcase in range(1,t+1):
    
    n = int(input())
    x = list(map(int, input().split()))
    hq = []
    for i in x:
        heapq.heappush(hq,i)
    
    result = 0
    n -=1
    while n > 0:
        n = (n-1)//2
        result+= hq[n]
    print(f'#{testcase} {result}')