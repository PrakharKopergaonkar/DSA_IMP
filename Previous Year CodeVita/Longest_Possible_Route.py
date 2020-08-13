import sys
def dfs(row,col,cost,matrix,row_dst,col_dst):
    if(row==row_dst and col==col_dst):
        return cost
    matrix[row][col] = -2
    cost_temp = -1
    if(row-1>=0 and matrix[row-1][col]==-1):
        cost_temp = max(cost_temp,dfs(row-1,col,cost+1,matrix,row_dst,col_dst))
    if(col-1>=0 and matrix[row][col-1]==-1):
        cost_temp = max(cost_temp,dfs(row,col-1,cost+1,matrix,row_dst,col_dst))
    if(row+1<len(matrix) and matrix[row+1][col]==-1):
        cost_temp = max(cost_temp, dfs(row+1,col,cost+1,matrix,row_dst,col_dst))
        matrix[row][col] = 0
    if(col+1<len(matrix[0]) and matrix[row][col+1]==-1):
        cost_temp = max(cost_temp, dfs(row,col+1,cost+1,matrix,row_dst,col_dst))
    
    matrix[row][col] = -1
    return cost_temp
M, N = map(int, input().split(' '))
H = int(input())
hurdles = []
matrix = [[-1 for i in range(0,N)] for j in range(0,M)]
for i in range(H):
    pointA, pointB = map(int, input().split(' '))
    hurdles.append([pointA,pointB])
    matrix[pointA][pointB] = -2
    
A1, A2 = map(int, input().split(' '))
B1, B2 = map(int, input().split(' '))

if([A1,A2] in hurdles or [B1,B2] in hurdles):
    print(-1)
else:
    print(dfs(A1,A2,0,matrix,B1,B2))
    
