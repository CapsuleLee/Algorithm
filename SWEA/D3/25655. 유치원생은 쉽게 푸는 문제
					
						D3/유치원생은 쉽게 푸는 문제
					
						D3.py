t = int(input())

for testcase in range(1,t+1):
    
    n = int(input())
    count8 = n//2
    count0 = n%2
    result =""

    if n ==1:
        result = "0"
    else:
        result ="4"*count0 + "8"*count8


    print(result)