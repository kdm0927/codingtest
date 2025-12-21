def solution(name):
    # 1. 상하 이동 횟수 계산 (알파벳 변경 비용)
    # 각 문자에 대해 위로 조작하는 것과 아래로 조작하는 것 중 작은 값을 더함
    spell_move = 0
    for char in name:
        spell_move += min(ord(char) - ord('A'), 26 - (ord(char) - ord('A')))
    
    # 2. 좌우 이동 횟수 계산 (커서 이동 비용)
    n = len(name)
    min_move = n - 1  # 기본값: 오른쪽으로만 쭉 가는 경우
    
    for i in range(n):
        # 현재 위치 i에서 다음 'A'가 아닌 문자의 위치(next_i)를 찾음
        next_i = i + 1
        while next_i < n and name[next_i] == 'A':
            next_i += 1
        
        
        # 방식 1: 0 -> i -> 0 -> next_i
        distance_r_l = i * 2 + (n - next_i)
        # 방식 2: 0 -> next_i -> 0 -> i
        distance_l_r = (n - next_i) * 2 + i
        
        min_move = min(min_move, distance_r_l, distance_l_r)
        
    return spell_move + min_move