from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self,U,V):
        self.graph[U].append(V)
    
    def BFS(self,s):
        queue = [s]
        visited = [False]*(len(self.graph))
        visited[s] = True
        bfs = []
        while(len(queue)>0):
            node = queue.pop(0)
            bfs.append(node)
            for i in self.graph[node]:
                if(not visited[i]):
                    queue.append(i)
                    visited[i] = True
        
        return bfs
    def getGraph(self):
        return self.graph

g = Graph()
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
print(g.BFS(2))
print(g.getGraph())

