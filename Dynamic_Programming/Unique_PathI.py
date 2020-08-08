class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0 for i in range(n)] for j in range(m)]
        matrix[-1][-1] = 1
        for i in range(len(matrix)-1,-1,-1):
            for j in range(len(matrix[0])-1,-1,-1):
                if(i+1<len(matrix)):
                    matrix[i][j] += matrix[i+1][j]
                
                if(j+1<len(matrix[0])):
                    matrix[i][j] += matrix[i][j+1]
        
        return matrix[0][0]

a = Solution()
row, column = map(int, input().split(' '))
print(a.uniquePaths(row,column))