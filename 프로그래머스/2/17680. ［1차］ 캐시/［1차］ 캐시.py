from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()

    for i in cities:
        i=i.lower()
        if cacheSize!=0 and i in cache:
            answer+=1
            cache.remove(i)
            cache.appendleft(i)
        else:
            answer+=5
            if cache and len(cache)>=cacheSize:
                cache.pop()
            cache.appendleft(i)
    print(answer)
    return answer