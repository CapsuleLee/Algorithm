t=int(input())

for testcase in range(1,t+1):
    a,b,n = map(int,input().split())
    count =0
    while n >= max(a,b):
        if a<b:
            a+=b
            count+=1
        else:
            b+=a
            count+=1

    print(count)