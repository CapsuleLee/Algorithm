import heapq

def solution(numbers):
    
    n=len(numbers)
    answer = [-1]*n
    heap=[]
    for i in range(n):
        num = numbers[i]
        
        while heap and heap[0][0] < num:
            value, idx = heapq.heappop(heap)
            answer[idx] = num
        heapq.heappush(heap,(num,i))
        
    return answer