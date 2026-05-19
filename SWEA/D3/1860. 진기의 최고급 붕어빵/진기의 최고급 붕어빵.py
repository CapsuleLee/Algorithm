t = int(input())

for testcase in range(1,t+1):
    n, m, k = map(int,input().split())
    time = list(map(int,input().split()))
    time.sort()

    count = [0] * (time[-1] + 1)
    flag = True
    
    for i in range(1, time[-1] + 1):
        if i % m == 0:
            count[i] =k
    for i in time:
        if count[i] > 0 or sum(count[:i]) > 0:
            count[i] -= 1
        else:
            print(f'#{testcase} Impossible')
            flag = False
            break
    if flag:
    
        print(f'#{testcase} Possible')