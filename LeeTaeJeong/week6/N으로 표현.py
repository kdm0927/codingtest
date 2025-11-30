def solution(N, number):

    dp = [set() for _ in range(9)] # 인덱스 0은 사용하지 않고 1부터 8까지 사용

    for i in range(1, 9):
        dp[i].add(int(str(N) * i))
        
    for i in range(1, 9): # i: N을 사용하는 총 횟수
        # i를 두 부분으로 나눔: j번 사용한 수와 i-j번 사용한 수의 연산
        for j in range(1, i): # j: 첫 번째 피연산자의 N 사용 횟수 (1 <= j < i)
            for a in dp[j]:
                for b in dp[i - j]:
                    # 덧셈
                    dp[i].add(a + b)
                    # 뺄셈 (b - a도 가능하지만 a - b와 (a - b) * -1 은 중복 가능성이 있으므로 두 경우 모두 고려)
                    dp[i].add(a - b)
                    # 곱셈
                    dp[i].add(a * b)
                    # 나눗셈 (나누기 연산에서 나머지는 무시하고 0으로 나누는 경우는 제외)
                    if b != 0:
                        dp[i].add(a // b)
                        
        # i번 사용해서 number를 만들 수 있는지 확인
        if number in dp[i]:
            return i

    # 8번까지 탐색했으나 number를 만들지 못한 경우
    return -1