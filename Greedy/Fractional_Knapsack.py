N, M = 7, 15
profit = 0
P = [10,5,15,7,6,18,3]
W = [2,3,5,7,1,4,1]

PW_ratio = [[round(P[i]/W[i],2),i] for i in range(0,N)]

PW_ratio.sort(key=lambda x: x[0], reverse=True)
ratio = [0]*N
i = 0
while(M>0):
    if(M - W[PW_ratio[i][1]]>=0):
        M-=W[PW_ratio[i][1]]
        ratio[PW_ratio[i][1]] = 1
    else:
        ratio[PW_ratio[i][1]] = round(M/W[PW_ratio[i][1]],2)
        M=0
    i+=1

for i in range(0,len(ratio)):
    profit+=ratio[i]*P[i]
print(ratio)
print(round(profit,2))