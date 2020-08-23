T = int(input())
for i in range(T):
    N = int(input())
    ranks = list(map(int, input().split(' ')))
    br = [0]*N
    br[0] = 1
    for i in range(1,N):
        if(ranks[i]>ranks[i-1]):
            br[i] = br[i-1]+1
        else:
            br[i] = 1
    
    summation = br[-1]
    for i in range(N-2,-1,-1):
        if(ranks[i]>ranks[i+1]):
            br[i] = br[i+1]+1
        else:
            br[i] = 1
        summation+=br[i]
    
    print(summation)