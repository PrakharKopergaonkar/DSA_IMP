N = int(input())

derangment = [0,1]
if(N==1 or N==2):
  print(derangment[N-1])
else:
    for i in range(3,N+1):
        derangment.append(((i-1)*(derangment[0]+derangment[1]))%(100000007))
        derangment.pop(0)


    print(derangment[1])