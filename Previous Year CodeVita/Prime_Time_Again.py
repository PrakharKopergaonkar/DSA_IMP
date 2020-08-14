D, P = map(int, input().split(' '))

if(D%P!=0):
    print(0)
else:
    isPrime = [True for i in range(0,D+1)]
    isPrime_subgroup = [True]*(D//P)
    isPrime[0] = False
    isPrime[1] = False
    for i in range(2,len(isPrime)):
        if(isPrime[i]):
            for j in range(i+i,len(isPrime),i):
                isPrime[j]= False
    
    for i in range(1,len(isPrime)):
        isPrime_subgroup[i%(D//P)] = isPrime_subgroup[i%(D//P)] and isPrime[i]
    counter=0
    for i in range(0,len(isPrime_subgroup)):
        if(isPrime_subgroup[i]):
            counter+=1
    
    print(counter)