import heapq, bisect
def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    while True:
        if bisect.bisect_left(scoville,K)<=0:
            break
        elif len(scoville)==1 and scoville[0]<K:
            answer = -1
            break
        temp1 = heapq.heappop(scoville)
        temp2 = heapq.heappop(scoville)
        temp3 = temp1+(temp2*2)
        heapq.heappush(scoville,temp3)
        answer+=1
        


    return answer