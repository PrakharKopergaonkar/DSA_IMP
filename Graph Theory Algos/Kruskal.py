class Graph:
    def __init__(self,V):
        self.V = V
        self.graph = []
    
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])
    
    def findParent(self, currentEdge, parent):
        if(parent[currentEdge]==currentEdge):
            return currentEdge
        else:
            return self.findParent(parent[currentEdge],parent)
    def KruskalMST(self):
        result = []
        total_cost = 0
        parent = [i for i in range(self.V)]

        #sort edges acc. to their weight
        self.graph = sorted(self.graph,key = lambda x: x[2])

        #Count to count number edges included and i to see which edge we are currently on
        count = 0
        i = 0

        while(count!=self.V-1):
            currentEdge = self.graph[i]

            #Check if we can add current edge in mst or not
            src_parent = self.findParent(currentEdge[0],parent)
            dst_parent = self.findParent(currentEdge[1],parent)

            if(src_parent!=dst_parent):
                result.append(currentEdge)
                count+=1
                parent[src_parent] = dst_parent
            i+=1

        return result
g = Graph(4) 
g.addEdge(0, 1, 10) 
g.addEdge(0, 2, 6) 
g.addEdge(0, 3, 5) 
g.addEdge(1, 3, 15) 
g.addEdge(2, 3, 4) 
  
print(g.KruskalMST()) 