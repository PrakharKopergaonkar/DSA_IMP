#code
import sys
T = int(input())
for i in range(T):
    N = int(input())
    nums = list(map(int, input().split(' ')))
    nums.sort()
    s1 = sum(nums)
    min_sum = sys.maxsize
    if(N>1):
        dp = [[False for j in range(s1+1)] for k in range(N+1)]
    
        for j in range(0,len(dp)):
            dp[j][0] = True
    
        
        for j in range(0,len(dp)):
            for k in range(0,len(dp[0])):
                dp[j][k] = dp[j-1][k]
            
                if(k>=nums[j-1]):
                    dp[j][k] = dp[j-1][k-nums[j-1]]
            
    
        for j in range(1,len(dp[0])-1):
            if(dp[N][j]):
                a = j
                b = s1 - j
                min_sum = min(min_sum, abs(a-b))
    
    else:
        min_sum = nums[0]
    
    print(min_sum)
    
 
    
    