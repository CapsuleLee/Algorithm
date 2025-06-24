t=int(input())

for _ in range(t):
    candy,box = map(int,input().split())
    temp=[]
    count=0
    for _ in range(box):
        r,c=map(int,input().split())
        temp.append(r*c)
    temp.sort(reverse=True)
    for i in temp:
        if candy<=0:
            print(count)
            break
        candy-=i
        count+=1