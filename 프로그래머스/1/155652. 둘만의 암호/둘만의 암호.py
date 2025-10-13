import sys
from collections import deque
import string

input = sys.stdin.readline

# lower_alph = {char: index for index, char in enumerate(string.ascii_lowercase)}
lower_alphabet = set([x for x in string.ascii_lowercase])

def solution(s, skip, index):
    answer = ''
    idx = 26 - len(skip)
    lower_alphabet_ = lower_alphabet-set(skip)
    lower_alphabet_list = sorted(lower_alphabet_)
    lower_alph={}
    for i in range(idx):
        lower_alph[lower_alphabet_list[i]] = i
    
    for i in s:
        answer+=lower_alphabet_list[(lower_alph[i]+index)% idx]
    
    return answer