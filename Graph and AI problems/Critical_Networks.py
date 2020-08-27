#Much similiar to Critical Planets asked in codevita zone-1 2020
#Question - Critical Connections in a Network
#Link - https://leetcode.com/problems/critical-connections-in-a-network/
from collections import defaultdict
import sys
class Solution:
    def __init__(self):
        self.Time = 0
        self.graph = defaultdict(list)
        self.bridges = []
    
    def BridgeUtil(self,u,In,visited,low,parent):
        visited[u] = True
        In[u] = self.Time
        low[u] = self.Time
        self.Time+=1
        for i in self.graph[u]:
            if(not visited[i]):
                parent[i] = u
                self.BridgeUtil(i,In,visited,low,parent)
                low[u] = min(low[u], low[i])
                if(low[i]>In[u]):
                    self.bridges.append([u,i])

            elif(i!=parent[u]):
                low[u] = min(low[u],In[i])
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        visited = [False]*(n)
        In = [sys.maxsize]*(n) #In time indicates when you entered the node
        low = [sys.maxsize]*(n) #low time indicates lowest ancestor where you can reach
        parent = [-1]*(n)
        
        for i in range(0,len(connections)):
            self.graph[connections[i][0]].append(connections[i][1])
            self.graph[connections[i][1]].append(connections[i][0])
            
        for i in range(0,n):
            if(not visited[i]):
                self.BridgeUtil(i,In,visited,low,parent)

        return self.bridges