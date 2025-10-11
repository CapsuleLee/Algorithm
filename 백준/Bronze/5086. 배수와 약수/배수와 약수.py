import sys

input = sys.stdin.readline

while True:
    n,m = map(int,input().split())
    if n == 0 and m == 0:
        break
    
    if n % m ==0: #두 번째 수가 첫 번째 수의 약수
        print("multiple")
        continue
    elif m%n ==0: #첫 번째 수가 두 번째 수의 약수
        print("factor")
        continue
    else:
        print("neither")