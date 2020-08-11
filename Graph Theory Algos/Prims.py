import sys
class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = [[0 for i in range(0,vertices)] for j in range(0,vertices)]
    
    def findminkey(self,visited,key):
        min_key = sys.maxsize
        for i in range(self.V):
            if(not visited[i] and key[i]<min_key):
                min_key = key[i]
                index = i
        
        return index
    def primMST(self):
        visited = [False]*self.V
        key = [sys.maxsize]*(self.V)
        key[0] = 0
        for i in range(0,self.V):
            min_key = self.findminkey(visited,key)
            visited[min_key] = True

            for j in range(0,self.V):
                if(not visited[j] and self.graph[min_key][j]>0):
                    key[j] = min(key[j],self.graph[min_key][j])
        
        
        return sum(key)
g = Graph(5)
g.graph = [ [0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]]
 
print(g.primMST())