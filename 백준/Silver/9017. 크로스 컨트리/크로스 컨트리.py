import sys
from collections import Counter, defaultdict

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    race = list(map(int, input().split()))

    # 1. 팀별 주자 수를 세고, 6명 이상인 유효팀을 가려냅니다.
    team_counts = Counter(race)
    valid_teams = {team for team, count in team_counts.items() if count >= 6}

    # 2. 유효팀 주자들의 등수를 순서대로 기록합니다.
    scores = defaultdict(list)
    rank = 1
    for team_num in race:
        if team_num in valid_teams:
            scores[team_num].append(rank)
            rank += 1

    # 3. 각 팀의 점수(상위 4명 합)와 5번째 주자 등수를 리스트에 저장합니다.
    final_results = []
    for team, ranks in scores.items():
        score = sum(ranks[:4])
        fifth_runner_rank = ranks[4]
        final_results.append((score, fifth_runner_rank, team))

    # 4. 점수 -> 5번째 주자 등수 순으로 정렬하여 우승팀을 찾습니다.
    final_results.sort()
    print(final_results[0][2])