import sys

a,b=map(int,sys.stdin.readline().split())
count=1
while True:
    if a==b:
        print(count)
        break
    elif a>b:
        print(-1)
        break

    if b%2==0:  #짝수 일때
        b=b/2    
        count+=1
        
    
    elif b%10 ==1:
        b-=1
        b=b//10
        count+=1
    else:
        print(-1)
        break