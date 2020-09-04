#The solution is of time complexity O(n) and space complexity O(1)
#The solution is two pass algorithm counting number of 0, 1 and 2 and appending them in next pass
#The more efficient is one pass algorithm 

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_0 = 0
        count_1 = 0
        count_2 = 0
        for i in nums:
            if(i==0):
                count_0+=1
            elif(i==1):
                count_1+=1
            else:
                count_2+=1
        
        for i in range(0,len(nums)):
            if(i<count_0):
                nums[i] = 0
            elif(i<count_0 + count_1):
                nums[i] = 1
            else:
                nums[i] = 2
        