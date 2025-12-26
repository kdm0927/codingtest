from itertools import permutations

def check_match(user, pattern):
    
    if len(user) != len(pattern):
        return False
    
    for u, p in zip(user, pattern):
        if p != '*' and u != p:
            return False
    return True

def solution(user_id, banned_id):
    answer_sets = set()
    
    # 1. user_id 중 banned_id의 개수만큼 뽑아서 줄 세우기 (순열)
    for perm in permutations(user_id, len(banned_id)):
        is_possible = True
        
        # 2. 뽑은 순열의 각 아이디가 banned_id의 패턴과 1:1로 매칭되는지 확인
        for i in range(len(banned_id)):
            if not check_match(perm[i], banned_id[i]):
                is_possible = False
                break
        
        # 3. 모든 아이디가 패턴과 일치한다면 결과 집합에 추가
        if is_possible:
            answer_sets.add(frozenset(perm))
            
    return len(answer_sets)