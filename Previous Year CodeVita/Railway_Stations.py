N = int(input())
arrival = []
departure = []
for i in range(N):
    ar, dt = map(int, input().split(' '))
    arrival.append(ar)
    departure.append(ar+dt)

i, j = 1, 0
points = 1
max_points = 1
while(i<N and j<N):
    if(arrival[i]<=departure[j]):
        points+=1
        i+=1
    else:
        points-=1
        j+=1
    max_points = max(max_points,points)

print(max_points)


