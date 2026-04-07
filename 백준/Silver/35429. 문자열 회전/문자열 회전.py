import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
word = list(map(str, input().strip()))

dic = defaultdict(int)


for i in word:
    dic[i] += 1

count = min(dic['G'],dic["S"]//2, dic["H"])
print(count)