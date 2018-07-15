print("The matrix should be square matrix:")
m = int(input("Enter the number of rows "))
n = int(input("Enter the number of columns "))
matrix =[]
transpose = []
for i in range(0,m):
     matrix.append([])
     transpose.append([])
for i in range (0,m):
    for j in range(0,n):
        matrix[i].append(j)
        matrix[i][j]=0
        transpose[i].append(j)
        transpose[i][j]=0     
for i in range (0,m):
     for j in range(0,n):
         print("value in row ", i+1, " and value in column", j+1)
         matrix[i][j] = int(input())

for i in range(0,m):
     for j in range(0,n):
          transpose[i][j] = matrix[j][i]
          print(transpose[i][j], end=" ")
     print("\n")