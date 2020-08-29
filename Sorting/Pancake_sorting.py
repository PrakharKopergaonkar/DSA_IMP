class Solution:
    def findindex(self,end,A):
        for i in range(0,len(A)):
            if(A[i]==end):
                return i
    
    def flip(self,index,A):
        b = A[0:index]
        A = b[::-1] + A[index:]
        return A
    def pancakeSort(self, A: List[int]) -> List[int]:
        output_list = []
        flips = 0
        end = len(A)
        while(end>1):
            index = self.findindex(end,A)
            A = self.flip(index+1,A)
            A = self.flip(end,A)
            output_list.append(index+1)
            output_list.append(end)
            end-=1

        print(A) 
        return output_list
    
a = Solution()
print(a.pancakeSort([3,2,4,1]))