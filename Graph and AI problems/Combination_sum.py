class Solution:
    def __init__(self):
        self.output_list = []
    
    def dfs(self,k,n,list1):
        if(k==0 and n==0):
            self.output_list.append(list1)
            return
        elif(k==0):
            return
        elif(len(list1)==0):
            i=1
        else:
            i=list1[-1]+1
        while(i<=min(n,9)):
            self.dfs(k-1,n-i,list1 + [i])
            i+=1
    def combinationSum3(self, k: int, n: int):
        self.dfs(k,n,[])
        
        return self.output_list
    
a = Solution()
print(a.combinationSum3(3,10))