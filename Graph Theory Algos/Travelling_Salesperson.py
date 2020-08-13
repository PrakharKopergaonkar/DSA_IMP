import sys
class Graph:
    def __init__(self,graph):
        self.graph = graph
        self.V = len(graph)

    def travellingSalesUtil(self,visited,source,nodes_visited):
        if(nodes_visited==self.V):
            return self.graph[source][0]
        else:
            min_path = sys.maxsize
            for i in range(0,self.V):
                if(self.graph[source][i]>0 and visited[i]==False):
                    visited[source] = True
                    min_path = min(min_path,self.travellingSalesUtil(visited,i,nodes_visited+1)+self.graph[source][i])
                    visited[source] = False
            return min_path
    def travellingSales(self,source):
        visited = [False]*(self.V)
        return self.travellingSalesUtil(visited,source,1)
        

graph = [[0, 10, 15, 20],[10, 0, 35, 25],[15, 35, 0, 30], [20, 25, 30, 0]] 

g = Graph(graph)
print(g.travellingSales(0))