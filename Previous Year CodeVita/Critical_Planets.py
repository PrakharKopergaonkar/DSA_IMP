#Find bridges in the graph and print in ascending order of findings

import sys
from collections import defaultdict
class Solution:
    def __init__(self,N,path):
        self.N = N
        self.Time = 0
        self.path = path
        self.bridges = []

    def BridgeUtil(self,u,In,visited,low,parent):
        visited[u] = True
        In[u] = self.Time
        low[u] = self.Time
        self.Time+=1
        for i in self.path[u]:
            if(not visited[i]):
                parent[i] = u
                self.BridgeUtil(i,In,visited,low,parent)
                low[u] = min(low[u], low[i])
                if(low[i]>In[u]):
                    self.bridges.append([u,i])

            elif(i!=parent[u]):
                low[u] = min(low[u],In[i])   
    def Bridge(self):
        visited = [False]*(self.N)
        In = [float('Inf')]*(self.N) #In time indicates when you entered the node
        low = [float('Inf')]*(self.N) #low time indicates lowest ancestor where you can reach
        parent = [-1]*(self.N)

        for i in range(0,self.N):
            if(not visited[i]):
                self.BridgeUtil(i,In,visited,low,parent)

        return self.bridges
M, N = map(int, input().split(' '))
path = defaultdict(list)

for i in range(0,M):
    paths_temp = list(map(int, input().split(' ')))
    path[paths_temp[0]].append(paths_temp[1])
    path[paths_temp[1]].append(paths_temp[0])

a = Solution(N,path)
result  = a.Bridge()
result = result[::-1]
visited = [False]*(N)
for i in range(0,len(result)):
    if(not visited[result[i][0]]):
        visited[result[i][0]] = True
        print(result[i][0])
    if(not visited[result[i][1]]):
        visited[result[i][1]] = True
        print(result[i][1]) 



