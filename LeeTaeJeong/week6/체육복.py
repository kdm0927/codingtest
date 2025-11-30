def solution(n, lost, reserve):
  
    lost_set = set(lost)
    reserve_set = set(reserve)
    
    # lost_set과 reserve_set의 교집합
    common = lost_set.intersection(reserve_set) 
    
    # 최종적으로 빌려줘야 하는 lost 목록과 빌려줄 수 있는 reserve 목록만 남김
    final_lost = lost_set - common
    final_reserve = reserve_set - common
    
    # 빌려줄 수 있는 reserve 학생들을 순회
    reserve_list = sorted(list(final_reserve)) 
    
    # 빌려주지 못한 lost 학생들을 담을 set
    for r in reserve_list:
        if r - 1 in final_lost:
            final_lost.remove(r - 1)
        elif r + 1 in final_lost:
            final_lost.remove(r + 1)
            
    # 최종적으로 체육 수업을 들을 수 있는 학생 수 = 전체 학생 수 - 빌려주지 못한 학생 수
    max_students = n - len(final_lost)
    
    return max_students