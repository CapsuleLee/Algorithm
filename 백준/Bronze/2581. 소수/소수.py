import sys

input = sys.stdin.readline

m=int(input())
n=int(input())

prime = []

def isPrime(num):
    if num ==1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i ==0:
            return False
        
    return True

for i in range(m,n+1):
    if isPrime(i):
        prime.append(i)
if prime:
    print(sum(prime))
    print(prime[0])
else:
    print(-1)