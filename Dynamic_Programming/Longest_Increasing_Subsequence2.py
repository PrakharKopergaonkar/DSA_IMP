#Solution 2 : Time Complexity - O(nlogn)

class Solution:
    def binarysearch(self,number, output_list):
        left = 0
        right = len(output_list)-1
        while(left<=right):
            mid = left + (right-left)//2
            if(output_list[mid]<number):
                left = mid + 1
            else:
                right = mid-1
        
        return left
    def lengthOfLIS(self, nums: List[int]) -> int:
        output_list = []
        for i in range(0,len(nums)):
            if(len(output_list)==0 or output_list[-1]<nums[i]):
                output_list.append(nums[i])
            
            else:
                index = self.binarysearch(nums[i],output_list)
                output_list[index] = nums[i]
        
        return len(output_list)

nums = [10,9,2,5,3,7,101,18]
a = Solution()
print(a.lengthOfLIS(nums))