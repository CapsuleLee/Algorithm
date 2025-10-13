import sys
from itertools import combinations

input = sys.stdin.readline

def isPrime(num):
    if num == 1:
        return False
    
    for i in range(2,int(num ** 0.5)+1):
        if num % i ==0:
            return False
    return True

def solution(nums):
    answer = 0
    temp =list(combinations(nums,3))
    
    for i in temp:
        total = sum(i)
        if isPrime(total):
            answer+=1
        
    return answer
