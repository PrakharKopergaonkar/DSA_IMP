N = int(input())
matrix = [[0 for i in range(N)] for j in range(N)]

first_row, last_row, first_col, last_col =  0, N, 0, N
all_pluspoints = [(0,0)]
counter = 1
plus_points = 1
while(first_row<last_row):
    for i in range(first_col,last_col):
        matrix[first_row][i] = counter
        if(counter%11==0):
            plus_points+=1
            all_pluspoints.append((first_row,i))
        counter+=1   
    first_row+=1

    for i in range(first_row,last_row):
        matrix[i][last_col-1] = counter
        if(counter%11==0):
            plus_points+=1
            all_pluspoints.append((i,last_col-1))
        counter+=1
    last_col-=1

    for i in range(last_col-1,first_col-1,-1):
        matrix[last_row-1][i] = counter
        if(counter%11==0):
            plus_points+=1
            all_pluspoints.append((last_row-1,i))
        counter+=1
    last_row-=1

    for i in range(last_row-1,first_row-1,-1):
        matrix[i][first_col] = counter
        if(counter%11==0):
            plus_points+=1
            all_pluspoints.append((i,first_col))
        counter+=1
    first_col+=1

for i in range(0,len(matrix)):
    for j in range(0,len(matrix[0])):
        print(matrix[i][j],end=" ")
    print(end="\n")

print("Total Power points : {}".format(plus_points))
for i in all_pluspoints:
    print("({},{})".format(i[0],i[1]))