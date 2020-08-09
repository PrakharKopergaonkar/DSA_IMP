#Algorithm works following way:
# 1. we initially store all the rotten oranges node inside queue
# 2. we continue a popping from queue untill its empty
# 3. we check for unrotten oranges adjacent to popped Node in grid and append them in queue if present
# 4. We also continue to update our max time that is required.
# 5. At the end we check if all our all oranges have rotten sucessfully and return result accordingly.  

import sys
#Orange Node for storing rotten oranges data
class orangeNode :
    def __init__(self,x,y,time):
        self.time = time
        self.x = x
        self.y = y
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        unrotten = 0
        time = -sys.maxsize
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if(grid[i][j]==2):
                    queue.append(orangeNode(i,j,0))
                elif(grid[i][j]==1):
                    unrotten+=1
        while(len(queue)):
            curr_Node = queue.pop(0)
            time = max(time,curr_Node.time)
            if(curr_Node.x+1<len(grid) and grid[curr_Node.x+1][curr_Node.y]==1):
                unrotten-=1
                grid[curr_Node.x+1][curr_Node.y] = 2
                queue.append(orangeNode(curr_Node.x+1,curr_Node.y,curr_Node.time+1))
            if(curr_Node.x-1>=0 and grid[curr_Node.x-1][curr_Node.y]==1):
                unrotten-=1
                grid[curr_Node.x-1][curr_Node.y]=2
                queue.append(orangeNode(curr_Node.x-1,curr_Node.y,curr_Node.time+1))
            if(curr_Node.y+1<len(grid[0]) and grid[curr_Node.x][curr_Node.y+1]==1):
                unrotten-=1
                grid[curr_Node.x][curr_Node.y+1] = 2
                queue.append(orangeNode(curr_Node.x,curr_Node.y+1,curr_Node.time+1))
            if(curr_Node.y-1>=0 and grid[curr_Node.x][curr_Node.y-1]==1):
                unrotten-=1
                grid[curr_Node.x][curr_Node.y-1] = 2
                queue.append(orangeNode(curr_Node.x,curr_Node.y-1,curr_Node.time+1))
            
        if(unrotten>0):
            return -1
        elif(time!=-sys.maxsize):
            return time
        else:
            return 0
        
a = Solution()
print(a.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))