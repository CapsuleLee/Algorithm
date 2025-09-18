import sys
input = sys.stdin.readline

n=int(input())

book=[]

for _ in range(n):
    book.append(int(input()))

maxNum = max(book)
count = 0

for i in range(-1,-n-1,-1):
    
    if book[i] == maxNum:
        count+=1
        maxNum-=1

print(n-count)