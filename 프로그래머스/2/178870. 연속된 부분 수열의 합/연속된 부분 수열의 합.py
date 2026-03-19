def solution(sequence, k):
    answer = [0]
    result = []
    prefix_sum = 0

    for i in sequence:
        prefix_sum += i
        answer.append(prefix_sum)
    right = 0
    left = 0
    min_len = len(answer) + 1
    
    while right < len(answer):
        currentSum = answer[right] - answer[left]
        if currentSum == k:
            currentLen = right - left
            if currentLen < min_len:
                min_len = currentLen
                result = [left, right-1]
            right +=1
        elif currentSum < k:
            right += 1
        else:
            left += 1
    
    return result