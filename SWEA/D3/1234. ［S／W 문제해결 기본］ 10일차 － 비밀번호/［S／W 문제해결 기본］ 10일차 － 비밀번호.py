for testcase in range(1,11):
    a, b = map(str,input().split())

    result = []

    for i in b:
        if result and result[-1] == i:
            result.pop()
            continue
        result.append(i)
    print(f'#{testcase} {"".join(result)}')