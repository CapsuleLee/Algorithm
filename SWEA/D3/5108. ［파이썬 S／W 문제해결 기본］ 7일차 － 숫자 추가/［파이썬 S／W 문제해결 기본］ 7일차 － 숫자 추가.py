
t=int(input())

for testcase in range(1,t+1):
    n,m,l = map(int,input().split())
    num = list(map(int,input().split()))

    for _ in range(m):
        a,b = map(int,input().split())
        num.insert(a,b)
 
    print(F"#{testcase}",num[l])