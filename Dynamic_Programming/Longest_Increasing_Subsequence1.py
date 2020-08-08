#Solution 1 : Time Complexity - O(n^2)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for i in range(0,len(nums))]
        
        max_number = 0
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if(nums[j]>nums[i] and dp[j]+1>dp[i]):
                    dp[i] = dp[j]+1
            
            
            max_number = max(dp[i],max_number)
        
        
        return max_number

nums = [10,9,2,5,3,7,101,18]
a = Solution()
print(a.lengthOfLIS(nums))