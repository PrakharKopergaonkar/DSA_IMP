N = int(input())

coins = [0,0,0]

if(N>4):
    coins[0] = (N-4)//5
    N -= ((N-4)//5) * 5

if(N>=2):
    if(N%2==1):
        coins[2] = 1
        N-=1
    else:
        coins[2] = 2
        N-=2

coins[1] = N//2

print(sum(coins),end=" ")
for i in coins:
    print(i,end=" ")
