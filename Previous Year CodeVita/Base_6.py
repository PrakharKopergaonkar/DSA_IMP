def base_6sum(number):
    return_number = 0
    while(number>=1):
        return_number+=number%6
        number=number//6
    return return_number


N = int(input())
arr = list(map(int, input().split(',')))

for i in range(0,N):
    arr[i] = base_6sum(arr[i])

output_number = 0
for i in range(0,len(arr)-1):
    for j in range(i+1,len(arr)):
        if(arr[j]<arr[i]):
            output_number+=1
print(output_number)