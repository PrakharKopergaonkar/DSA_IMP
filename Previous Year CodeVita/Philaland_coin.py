T = int(input())
for i in range(T):
    N = int(input())
    count = 0
    total = 0
    j=0
    while(True):
        count+=1
        total+=2**j
        j+=1
        if(total>=N):
            break    
    print(count)