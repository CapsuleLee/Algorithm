import sys

input = sys.stdin.readline

word=input().rstrip()
check=["U","C","P","C"]
count=0

for i in word:
    if i == check[count]:
        count+=1
    if count ==4:
        break
if count == 4:
    print("I love UCPC")
else:
    print("I hate UCPC")