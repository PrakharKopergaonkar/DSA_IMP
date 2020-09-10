# This problem is based on graph coloring and dfs 
# We pick every unvisited node check is graph coloring with 2 colors is possible while performing dfs on it.
from collections import defaultdict
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        self.graph = defaultdict(list)
        for i, j in dislikes:
            self.graph[i-1].append(j-1)
            self.graph[j-1].append(i-1)
        
        self.color = [-1]*(N)
        
        for i in range(0,N):
            if(self.color[i]==-1 and not self.dfs(i,0)):
                return False
        
        return True
    def dfs(self,pos,v):
        if(self.color[pos]==-1) : 
            self.color[pos] = v
        else:
            return self.color[pos] == v
            
        for i in self.graph[pos]:
            if(not self.dfs(i,1-v)):
                return False
        
        return True
                
                
        
        