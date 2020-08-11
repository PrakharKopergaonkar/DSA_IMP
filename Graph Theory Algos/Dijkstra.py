import sys
class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = [[0 for i in range(vertices)] for j in range(vertices)]
    
    def findMin(self,visited,cost):
        min_cost = sys.maxsize
        for i in range(0,self.V):
            if(not visited[i] and min_cost>cost[i]):
                min_cost = min(min_cost,cost[i])
                min_index = i
        return min_index
    def dijkstra(self,source):
        visited = [False]*(self.V)
        cost = [sys.maxsize]*(self.V)

        cost[source] = 0
        for i in range(0,self.V):
            min_vertex = self.findMin(visited,cost)
            visited[min_vertex] =True
            for j in range(0,self.V):
                if(not visited[j] and self.graph[min_vertex][j]>0):
                    cost[j] = min(cost[j],self.graph[min_vertex][j] + cost[min_vertex])
        
        return cost
g = Graph(9) 
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
        [4, 0, 8, 0, 0, 0, 0, 11, 0], 
        [0, 8, 0, 7, 0, 4, 0, 0, 2], 
        [0, 0, 7, 0, 9, 14, 0, 0, 0], 
        [0, 0, 0, 9, 0, 10, 0, 0, 0], 
        [0, 0, 4, 14, 10, 0, 2, 0, 0], 
        [0, 0, 0, 0, 0, 2, 0, 1, 6], 
        [8, 11, 0, 0, 0, 0, 1, 0, 7], 
        [0, 0, 2, 0, 0, 0, 6, 7, 0] 
        ]; 
  
print(g.dijkstra(0)) 
  