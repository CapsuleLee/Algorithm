from collections import defaultdict

t = int(input())

for testcase in range(1,t+1):
    
    word = input()
    d = defaultdict(int)
    result=[]
    for i in word:
        d[i] += 1
    for k,v in d.items():
        if v%2 == 1:
            result.append(k)
    result.sort()
    
    if result:
        print(f'#{testcase} {"".join(result)}')
    else:
        print(f'#{testcase} Good')