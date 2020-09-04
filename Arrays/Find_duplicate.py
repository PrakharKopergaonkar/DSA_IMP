#The solution uses turtoise Hare method.
#In the loop we find the cycle in the array
#In the second we place one pointer at the starting while second one keeps rotating in cycle
#The place where they meet is the duplicate number

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while(True):
            slow = nums[slow]
            fast = nums[nums[fast]]
            if(slow==fast):
                break
        
        fast = nums[0]
        while(slow!=fast):
            slow = nums[slow]
            fast = nums[fast]
        return fast

a = Solution()
print(a.findDuplicate([1,3,4,2,2]))