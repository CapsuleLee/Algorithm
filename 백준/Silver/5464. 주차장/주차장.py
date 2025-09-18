import sys
from collections import deque
import heapq
input = sys.stdin.readline

#n이 주차공간 수, m이 차량 수
n, m =map(int,input().split())

parking=[i for i in range(1,n+1)]

#주차장과 차 번호 매핑
parkingNumber = [0]*(m+1)
heapq.heapify(parking)

#주차요금
parkingFee=[0]*(n+1)
#자동차 무게
car=[0]*(m+1)
waitQ = deque()
exitQ = deque()
result = 0


for i in range(1,n+1):
    fee = int(input())
    parkingFee[i]=fee

for i in range(1,m+1):
    weight = int(input())
    car[i]=weight
    
for i in range(2*m):
    num = int(input())
    #주차장이 꽉 찼을때    
    if m-parkingNumber.count(0)+1 == n and num > 0:
        waitQ.append(num)
        continue
    elif num < 0:
        heapq.heappush(parking,parkingNumber[abs(num)])
        parkingNumber[abs(num)] = 0
        if waitQ:
            num = waitQ.popleft()
            parkingNum = heapq.heappop(parking)
            parkingNumber[num] = parkingNum
            result += car[num] * parkingFee[parkingNum]
    else: #주차장이 자리 있을때
        if parking:
            parkingNum = heapq.heappop(parking)
            parkingNumber[num] = parkingNum
            result += car[num] * parkingFee[parkingNum]
            
   
print(result)