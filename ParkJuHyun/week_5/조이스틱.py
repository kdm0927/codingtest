def solution(name):
    answer = 0
    
    for c in name:
        answer += min(ord(c)-ord('A'), 26 - (ord(c)-ord('A')))

    n = len(name)
    min_move = n-1
    
    for i in range(n):
        next_idx = i+1
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
        
        distance = min(i,n - next_idx)
        min_move = min(min_move, i + n - next_idx + distance)
    
    answer += min_move
    return answer