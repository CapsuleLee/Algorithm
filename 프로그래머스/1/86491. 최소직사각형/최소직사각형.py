def solution(sizes):
    for i in sizes:
        if i[0] < i[1]:
            i[0], i[1] = i[1],i[0]
    max0, max1=0,0
    for i in sizes:
        if max0<i[0]:
            max0 = i[0]
        if max1< i[1]:
            max1 = i[1]
    return int(max0 * max1)