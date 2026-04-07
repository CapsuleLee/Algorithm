import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    num = list(map(int,input().split()))    
    dic = defaultdict(int)
    criteria = num[0] //2
    for i in num[1:]:
        dic[i] += 1
    result = sorted(list(dic.items()), key = lambda x:(-x[1]))
    if criteria < result[0][1]:
        print(result[0][0])
    else:
        print("SYJKGW")
