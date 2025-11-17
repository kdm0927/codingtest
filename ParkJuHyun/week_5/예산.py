def solution(d, budget):
    answer = 0
    left = budget
    
    d.sort()
    
    for _ in d:
        if left>= _:
            answer += 1
            left -= _
        else:
            break
    
    return answer