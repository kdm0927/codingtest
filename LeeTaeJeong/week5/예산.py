def solution(d, budget):
    answer = 0
    
    # 1. 신청 금액이 적은 순서대로 정렬합니다. (오름차순)
    d.sort()
    
    # 2. 적은 금액부터 차례대로 예산에서 뺍니다.
    for amount in d:
        if budget >= amount:
            budget -= amount
            answer += 1
        else:
            # 예산이 부족하면 더 이상 지원할 수 없으므로 반복을 종료합니다.
            # (뒤에 있는 부서들은 현재 amount보다 더 큰 금액을 요구하므로 볼 필요가 없습니다)
            break
            
    return answer