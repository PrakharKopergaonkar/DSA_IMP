import heapq
N = int(input())
cities = list(map(int, input().split(' ')))
M = int(input())

if(len(cities)<=1 or cities[-1]==-1):
    print(-1)
else:
    cost = cities[0] + cities[-1]
    cities = cities[1:len(cities)-1]
    heapq.heapify(cities)

    for i in range(0,len(cities)):
        if(cities[i]==-1):
            M-=1
        else:
            cost+=cities[i]
    if(M<0):
        print(-1)
    else:
        print(cost - sum(heapq.nlargest(M,cities)))

