t=int(input())

for testcase in range(1,t+1):

    horns, animals = map(int,input().split())

    print(F"#{testcase}",horns-(horns-animals)*2,horns-animals)