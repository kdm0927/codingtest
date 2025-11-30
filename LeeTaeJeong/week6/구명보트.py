from collections import deque

def solution(people, limit):
    #사람들의 몸무게를 오름차순으로 정렬
    people.sort()
    
    answer = 0
    light = 0           # 가장 가벼운 사람을 가리키는 인덱스 (왼쪽 끝)
    heavy = len(people) - 1 # 가장 무거운 사람을 가리키는 인덱스 (오른쪽 끝)
    
    while light <= heavy:
        answer += 1
        
        # 가장 무거운 사람은 무조건 태움
        # 가장 가벼운 사람을 함께 태울 수 있는지 확인
        if people[light] + people[heavy] <= limit:
            # 함께 탈 수 있다면, 가장 가벼운 사람도 보트에 태움
            light += 1  # 다음으로 가벼운 사람을 처리
            
        # heavy는 보트에 태워졌으므로 무조건 다음으로 무거운 사람을 처리
        heavy -= 1
        
    return answer