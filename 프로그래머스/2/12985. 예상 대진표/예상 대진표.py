import math
def solution(n,a,b):

    lv=1
    while True:
        if math.ceil(a/2) ==math.ceil(b/2):
            return lv
        a=math.ceil(a/2)
        b=math.ceil(b/2)
        lv+=1