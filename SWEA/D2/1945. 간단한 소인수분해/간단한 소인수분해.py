from collections import defaultdict

t = int(input())

for testcase in range(1,t+1):
    n = int(input())
    check = defaultdict(int)

    for i in range(2, int(n**0.5)+1):
        while n % i == 0:
            check[i] += 1
            n //= i

    
    print(f'#{testcase} {check[2]} {check[3]} {check[5]} {check[7]} {check[11]}')