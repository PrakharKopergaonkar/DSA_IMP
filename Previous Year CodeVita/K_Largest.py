import math
N , K = map(int, input().split(' '))

output_list = []
res = -1
for i in range(1,int(math.sqrt(N))+1):
    if(N%i==0):
        output_list.append(i)
        if(N//i!=i):
            K-=1
            if(K==0):
                res = N//i
                break

if(res==-1 and K<=len(output_list)):
    res = output_list[-K]
elif(res==-1 and K>len(output_list)):
    res = 1

print(res)        