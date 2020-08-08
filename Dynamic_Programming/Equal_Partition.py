class Solution:
    def isEqual(self,nums,pos,target):
        if(target<0):
            return False
        elif(target==0):
            return True
        else:
            for i in range(pos+1,len(nums)):
                if(self.isEqual(nums,i,target-nums[i])):
                    return True
    def canPartition(self, nums: List[int]) -> bool:
        s1 = sum(nums)
        if(s1%2==1 or len(nums)<=1) : 
            return False
        
        nums.sort(reverse=True)
        return self.isEqual(nums,0,s1//2-nums[0])