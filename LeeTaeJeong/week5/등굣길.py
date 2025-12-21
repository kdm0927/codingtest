def solution(m, n, puddles):
    # 1. DP 테이블 초기화
    # m이 가로(열), n이 세로(행)이므로 n행 m열의 격자를 만듭니다.
    # 인덱스 계산을 편하게 하기 위해 (n+1) x (m+1) 크기로 만듭니다.
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # 2. 시작점 초기화
    dp[1][1] = 1
    
    # 3. 반복문을 통해 각 좌표까지 가는 최단 경로 개수 계산
    for i in range(1, n + 1):       # 행 (y 좌표 해당)
        for j in range(1, m + 1):   # 열 (x 좌표 해당)
            # 시작점은 계산하지 않고 건너뜁니다 (이미 1로 설정함)
            if i == 1 and j == 1:
                continue
            
            # 웅덩이 확인: puddles는 [x, y] 순서로 주어집니다.
            # 현재 좌표 (j, i)가 웅덩이인지 확인합니다.
            if [j, i] in puddles:
                dp[i][j] = 0
            else:
                # 현재 칸 = 위쪽 칸 + 왼쪽 칸
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007
                
    # 도착 지점 (n, m)의 값 반환
    return dp[n][m]