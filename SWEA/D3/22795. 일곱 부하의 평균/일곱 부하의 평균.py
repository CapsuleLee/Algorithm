t=int(input())

for testcase in range(1,t+1):

    a = list(map(int,input().split()))
    total = sum(a)
    result = max(a)

    while True:
        result += 1
        if (total + result)%7 == 0 :
            print(result)
            break