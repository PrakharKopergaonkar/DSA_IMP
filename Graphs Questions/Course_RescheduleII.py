#Based on Topological Sorting and cycle detection
#LeetCode Link - https://leetcode.com/problems/course-schedule-ii/

from collections import defaultdict
class Solution:
    def dfs(self,graph,visited,schedule,curr_node):
        visited[curr_node] = 1
        for i in graph[curr_node]:
            if(visited[i]==1):
                return True
            elif(visited[i]==0 and self.dfs(graph,visited,schedule,i)):
                return True
        
        schedule.append(curr_node)
        visited[curr_node] = 2
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for i in range(0,len(prerequisites)):
            graph[prerequisites[i][0]].append(prerequisites[i][1])
        
        visited = [0]*numCourses
        schedule = []
        for i in range(0,numCourses):
            if(visited[i]==0 and self.dfs(graph,visited,schedule,i)):
                return []
        
        return schedule