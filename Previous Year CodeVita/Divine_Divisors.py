import math
N = int(input())
output_list = []
for i in range(1,int(math.sqrt(N))+1):
    if(N%i==0):
        print(i,end=" ")
        if(N//i!=i):
            output_list.append(N//i)

for i in range(len(output_list)-1,-1,-1):
    print(output_list[i],end=" ")