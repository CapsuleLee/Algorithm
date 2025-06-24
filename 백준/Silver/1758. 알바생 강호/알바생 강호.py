n=int(input())
starbucks=[]
for _ in range(n):
    x=int(input())
    starbucks.append(x)

starbucks.sort(reverse=True)
sum=0
idx=1
for i in starbucks:
    
    cost = i-(idx-1)
    if cost<=0:
        continue
    else:
        sum+=cost
    idx+=1
print(sum)