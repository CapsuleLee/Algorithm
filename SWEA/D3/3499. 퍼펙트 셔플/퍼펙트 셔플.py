t = int(input())

for testcase in range(1,t+1):
    
    n = int(input())
    card = list(map(str, input().split()))
    if n%2 == 1:
        n+=1
    a= card[:n//2]
    b= card[n//2:]
    result=[]
    flag = True
    
    for i in range(len(card)):
        if flag:
            result.append(a.pop(0))
            flag = False
        else:
            result.append(b.pop(0))
            flag = True

    print('#'+str(testcase), *result)