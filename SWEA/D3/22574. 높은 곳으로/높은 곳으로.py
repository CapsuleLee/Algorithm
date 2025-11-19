t=int(input())

for testcase in range(1,t+1):
    n, p = map(int,input().split())
    count = 0

    for i in range(1,n+1):
        count += i
        if count == p:
            count -= 1

    print(count)