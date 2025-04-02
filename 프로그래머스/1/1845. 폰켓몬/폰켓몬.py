def solution(nums):
    answer = 0
    num=len(nums)//2
    result=set(nums)
    if num < len(result):
        return num
    return len(result)