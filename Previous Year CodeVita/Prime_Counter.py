T = int(input())

for i in range(0,T):
    counter=0
    L,R = map(int, input().split(' '))
    isPrime = [False if(i%2==0) else True for i in range(0,R+1)]
    if(len(isPrime)>=2):
        isPrime[1] = False
    if(len(isPrime)>=3):
        isPrime[2] = True
    
    for i in range(3,len(isPrime)):
        if(isPrime[i]):
            for j in range(i+i,len(isPrime),i):
                isPrime[j] = False

    count_Primes = [0]*(R+1)
    for j in range(2,len(count_Primes)):
        if(isPrime[j]):
            count_Primes[j] = 1 + count_Primes[j-1]
        else:
            count_Primes[j] = count_Primes[j-1]
     
        if(j>=L and j<=R and isPrime[count_Primes[j]]):
            counter+=1
    
    print(counter)