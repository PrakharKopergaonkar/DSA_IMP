N = int(input())

arr = list(map(int, input().split(' ')))

xor_sum = 0
for i in range(0,len(arr)):
    xor_sum = xor_sum^arr[i]


if(xor_sum==0):
    print("JASBIR")

else:
    print("AMAN")