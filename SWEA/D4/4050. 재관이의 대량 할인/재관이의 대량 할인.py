t = int(input())

for testcase in range(1,t+1):
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    result = 0
    
    while x:
        temp = []
        if len(x) < 3:
            result+=sum(x)
            break
        else:
            for i in range(3):
                if x:
                    temp.append(x.pop())
            temp.pop()
            result+=sum(temp)

    print(f'#{testcase} {result}')