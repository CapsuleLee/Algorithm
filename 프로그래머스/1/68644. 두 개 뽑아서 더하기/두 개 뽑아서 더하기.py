def solution(numbers):
    answer = []
    temp=set()
    length = len(numbers)
    for i in range(length-1):
        for j in range(i+1,length):
            temp.add(numbers[i]+numbers[j])
    answer = sorted(temp)
    return answer