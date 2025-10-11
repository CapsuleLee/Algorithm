import sys

input = sys.stdin.readline

T = int(input())

def GCD(a,b):
    while b>0:
        a,b = b,a%b
    return a

for _ in range(T):
    a,b = map(int,input().split())
    print(a*b//GCD(a,b))