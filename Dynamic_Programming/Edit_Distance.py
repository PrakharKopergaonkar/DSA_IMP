class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        matrix = [[0 for i in range(0,len(word2)+1)] for j in range(0,len(word1)+1)]
        
        for i in range(0,len(matrix[0])):
            matrix[0][i] = i
        
        for i in range(0,len(matrix)):
            matrix[i][0] = i
            
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if(word1[i-1]==word2[j-1]):
                    matrix[i][j] = matrix[i-1][j-1]
                else:
                    matrix[i][j] = min(matrix[i][j-1],matrix[i-1][j-1],matrix[i-1][j])+1
        
        return matrix[-1][-1]


a = Solution()
word1 = "intention"
word2 = "execution"
print(a.minDistance(word1,word2))