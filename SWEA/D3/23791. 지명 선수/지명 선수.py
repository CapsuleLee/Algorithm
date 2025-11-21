t=int(input())

for testcase in range(1,t+1):

    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int, input().split()))
    answer=""
    result =[0]*n
    check = set()
    turn = True
    for i in range(n):
        if turn: #A팀 뽑을 차례
            temp = a.pop(0)
            while temp in check:
                temp = a.pop(0)
            result[temp-1]="A"
            check.add(temp)
            turn = False

        else: #B팀 뽑을 차례
            temp = b.pop(0)
            while temp in check:
                temp = b.pop(0)
            result[temp-1] = "B"
            check.add(temp)
            turn = True

    for i in result:
        answer+=i
    print(answer)