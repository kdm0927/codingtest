def solution(m, n, puddles):
    arr = [[0]*m for _ in range(n)]
    arr[0][0] = 1
    
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
                
            if [j+1,i+1] in puddles:
                arr[i][j] = 0
                
            else:
                up = arr[i-1][j] if i > 0 else 0
                
                left = arr[i][j-1] if j > 0 else 0 
                
                arr[i][j] = (up + left) % 1000000007
    
    return arr[n-1][m-1]