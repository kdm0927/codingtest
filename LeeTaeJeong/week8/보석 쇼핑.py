def solution(gems):
    # 1. 전체 보석 종류 개수 파악
    total_kind = len(set(gems))
    N = len(gems)
    
    # 결과값 초기화 (최대 길이보다 크게 설정)
    answer = [1, N]
    min_len = N + 1
    
    # 딕셔너리 및 투 포인터 초기화
    gem_dict = {}
    start = 0
    end = 0
    
    while end < N:
        # 2. 윈도우 확장: end 포인터의 보석 추가
        now_gem = gems[end]
        gem_dict[now_gem] = gem_dict.get(now_gem, 0) + 1
        end += 1
        
        # 3. 모든 종류의 보석을 포함하고 있는지 확인
        if len(gem_dict) == total_kind:
            
            # 4. 윈도우 축소: start 포인터를 이동하며 불필요한 보석 제거
            # start 지점의 보석이 2개 이상이면 하나 빼고 start를 뒤로 미뤄도 여전히 조건 만족함
            while start < end:
                if gem_dict[gems[start]] > 1:
                    gem_dict[gems[start]] -= 1
                    start += 1
                else:
                    break
            
            # 5. 최솟값 갱신: 현재 구간 길이가 최소라면 정답 업데이트
            # end는 이미 +1 된 상태이므로 현재 길이는 (end - start)
            if (end - start) < min_len:
                min_len = end - start
                answer = [start + 1, end] # 문제는 1-based index
                
    return answer