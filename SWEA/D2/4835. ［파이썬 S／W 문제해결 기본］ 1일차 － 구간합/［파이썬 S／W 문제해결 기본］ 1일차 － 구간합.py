t=int(input())

for testcase in range(1,t+1):

    n,m = map(int,input().split())
    x=list(map(int,input().split()))
    result=[]
    for i in range(n-m+1):
        result.append(sum(x[i:i+m]))
 
    print(F"#{testcase}",max(result)-min(result))