# Type your code here
N = int(input())
if(N>=4):
    isPrime = [False if(i%2==0) else True for i in range(0,N+1)]
    isPrime[2] = True
    for i in range(3,len(isPrime)):
        if(isPrime[i]):
            j = i+i
            while(j<=N):
                isPrime[j] = False
                j+=i
    
    counter = 0
    last_prime = 2
    for i in range(3,N+1):
        if(isPrime[i]):
            last_prime+=i
            if(last_prime <= N and isPrime[last_prime]):
                counter+=1
            elif(last_prime>N):
                break
    print(counter)
else:
  print(0)