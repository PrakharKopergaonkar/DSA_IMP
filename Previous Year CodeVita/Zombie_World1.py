import heapq
t = int(input())
for i in range(t):
    N, MT = map(int, input().split(' '))
    E = list(map(int, input().split(' ')))
    IE, ME = map(int, input().split(' '))

    if(MT<N):
        print("NO")
    else:
        heapq.heapify(E)
        flag = False
        while(len(E)>0):
            curr_Z = heapq.heappop(E)
            if(curr_Z>=IE):
                flag=True
                break
            else:
                IE += IE - curr_Z
        
        if(flag or IE<ME):
            print("NO")
        else:
            print("YES")