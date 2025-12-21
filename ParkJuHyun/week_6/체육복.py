def solution(n, lost, reserve):
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost)-set(reserve)
    
    for i in sorted(set_lost):
        if i-1 in set_reserve:
            set_reserve.remove(i-1)
        elif i+1 in set_reserve:
            set_reserve.remove(i+1)
        else:
            n-=1
            
    return n