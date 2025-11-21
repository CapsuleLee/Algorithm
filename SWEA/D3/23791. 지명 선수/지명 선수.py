
import collections

t=int(input())

for testcase in range(1,t+1):

    n = int(input())
    a = collections.deque(map(int,input().split()))
    b = collections.deque(map(int, input().split()))
    answer=""
    result =[0]*n
    check = set()
    turn = True
    for i in range(n):
        if turn: #A팀 뽑을 차례
            temp = a.popleft()
            while temp in check:
                temp = a.popleft()
            result[temp-1]="A"
            check.add(temp)
            turn = False

        else: #B팀 뽑을 차례
            temp = b.popleft()
            while temp in check:
                temp = b.popleft()
            result[temp-1] = "B"
            check.add(temp)
            turn = True

    for i in result:
        answer+=i
    print(answer)