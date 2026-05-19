t = int(input())

for testcase in range(1,t+1):
    n = input()
    count = 0
    flag = False # 1이면 True, 0이면 False
    for i in n:
        if flag == False and i == '1':
            count += 1
            flag = True
        elif flag and i =="0":
            count +=1
            flag = False
        
    print(f'#{testcase} {count}')