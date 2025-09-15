import sys
from collections import defaultdict, deque
input = sys.stdin.readline

nodeNum = int(input())

tree = defaultdict(list)

for _ in range(nodeNum):
    a,b,c = map(str,input().split())
    tree[a].append(b)
    tree[a].append(c)

def DFS(start): #전위 순회 끝
    
    print(start,end="")
    
    for i in tree[start]:
        if i =='.':
            continue
        DFS(i)
        
DFS('A')
print()

result = []
#중위순회
def DFS2(start): 
    
    if start != '.':
        DFS2(tree[start][0])
        print(start,end="")
        DFS2(tree[start][1])        
    

DFS2('A')
print()

#후위순회
def DFS3(start): 
    
    for i in tree[start]:
          
        DFS3(i)
        if i =='.':
            continue
        print(i,end="")
        
DFS3('A')
print('A')