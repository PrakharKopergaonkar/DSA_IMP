
N, K = map(int, input().split(' '))
summation = 0
factorial = [0]*(N+1)
factorial[0] = 1
for i in range(1,N+1):
    factorial[i] = i*factorial[i-1]


for i in range(0,K+1,2):
    summation+= factorial[N] // (factorial[i]*factorial[N-i])

print(summation%(10**9 + 7))

