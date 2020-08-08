class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        matrix = [[0 for i in range(0,len(text2))] for j in range(0,len(text1))]
        
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if(text1[i]==text2[j]):
                    if(i-1>=0 and j-1>=0):
                        matrix[i][j] = 1 + matrix[i-1][j-1]
                    else:
                        matrix[i][j] = 1
                else:
                    if(j-1>=0):
                        matrix[i][j] = max(maximum,matrix[i][j-1])
                    if(i-1>=0):
                        matrix[i][j]= max(maximum,matrix[i-1][j])
                    if(i-1>=0 and j-1>=0):
                        matrix[i][j] = max(maximum,matrix[i-1][j-1])
        
        return matrix[-1][-1]

a = Solution()
text1 = input()
text2 = input()
print(a.longestCommonSubsequence(text1,text2))