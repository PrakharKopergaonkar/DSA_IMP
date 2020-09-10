#LeetCode Link - https://leetcode.com/problems/image-overlap/
#The idea is to generate all possible translates and get maximum of ones over each other
#Time complexity - O(n^4)
#Space Complexity - O(1)

class Solution:
    def getones(self, x_shift, y_shift, A,B,size):
        count = 0
        for A_row, B_row in enumerate(range(x_shift,size)):
            for A_col, B_col in enumerate(range(y_shift,size)):
                if(A[A_row][A_col]==B[B_row][B_col] and A[A_row][A_col]==1):
                    count+=1
        
        return count
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        N = len(A) #Number of rows and column in matrix
        overlapping = 0
        for x_shift in range(0,N):
            for y_shift in range(0,N):
                overlapping = max(overlapping,self.getones(x_shift,y_shift,A,B,N),self.getones(x_shift,y_shift,B,A,N))
        
        return overlapping
                
                
                
                   