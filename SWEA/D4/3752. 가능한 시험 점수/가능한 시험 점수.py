
t = int(input())

for key in range(t):
    n = int(input())
    score = list(map(int,input().split()))
    total = {0}
    for i in score:
        new_score = [i + s for s in total]
        total.update(new_score)
    print(f'#{key+1} {len(total)}')