x=int(input())
z=2
while x!=1:

    if x%z!=0:
        z+=1
    else:
        x=x//z
        
        print(z)
        z=2
        