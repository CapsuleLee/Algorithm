t = int(input())

for testcase in range(1,t+1):
    n = int(input())
    answer ={0,1,2,3,4,5,6,7,8,9}
    check = set()
    temp = n
    while True:
        for i in str(temp):
            check.add(int(i))
        if check == answer:
            break
        temp +=n
        
    print(f'#{testcase} {temp}')