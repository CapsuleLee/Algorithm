t=int(input())

for testcase in range(1,t+1):

    n=int(input())
    result =[]
    count=0
    for _ in range(n):
        c,k = map(str,input().split())
        k=int(k)
        for idx in range(k):
            result.append(c)
    print(F"#{testcase}")
    for i in result:
        print(i,end="")
        count+=1
        if count == 10:
            count = 0
            print()
    if count != 0:
        print()
