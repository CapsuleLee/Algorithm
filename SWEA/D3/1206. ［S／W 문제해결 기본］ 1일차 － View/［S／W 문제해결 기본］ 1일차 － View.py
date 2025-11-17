for testcase in range(1,10+1):
    
    width = int(input())
    graph=[[0]*width for _ in range(255+1)]
    building = list(map(int,input().split()))
    count = 0
    for i in range(2,width-2):
        
        for j in range(building[i]+1):
            graph[j][i]=1
    for i in range(2,width-2):
       
        for j in range(building[i]+1):
            if graph[j][i-2] ==0 and graph[j][i-1] ==0 and graph[j][i+2] ==0 and graph[j][i+1] == 0:
                graph[j][i] = 2
                count+=1
    print(F"#{testcase}",count)