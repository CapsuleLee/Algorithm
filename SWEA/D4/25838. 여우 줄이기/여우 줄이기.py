t = int(input())

for testcase in range(1,t+1):
    n = int(input())
    word = input()

    stack = []

    for i in word:

        stack.append(i)
        if len(stack) >=3 and stack[-3:] ==['f','o','x']:
            stack.pop()
            stack.pop()
            stack.pop()

    print(f'{len(stack)}')