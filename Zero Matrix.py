zeroR = -1
zeroC = -1
for i in range(M):
    for j in range(N):
        if matrix[M][N] == 0:
            zeroR = M
            zeroC = N 
for i in range(M):
    matrix[M][zeroC] = 0
for j in range(N):
    matrix[zeroR][N] = 0
return matrix
