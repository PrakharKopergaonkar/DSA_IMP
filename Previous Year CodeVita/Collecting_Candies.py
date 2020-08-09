import heapq
T = int(input())

for i in range(0,T):
    N = int(input())
    candies = list(map(int, input().split(' ')))
    heapq.heapify(candies)
    time = 0
    while(len(candies)>1):
        a1 = heapq.heappop(candies)
        a2 = heapq.heappop(candies)
        time+=a1+a2
        heapq.heappush(candies,a1+a2)
    
    print(time);
