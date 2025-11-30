def solution(number, k):
    # 결과를 저장할 스택
    stack = []
    
    for num in number:

        # 스택의 마지막 원소가 현재 숫자보다 작다면 제거
        while stack and k > 0 and stack[-1] < num:
            stack.pop()  # 스택의 마지막 원소 제거
            k -= 1       # 제거 횟수 1 감소
        
        # 현재 숫자 삽입
        stack.append(num)
        
    if k > 0:
        # 최종 결과는 스택의 앞에서부터 len(stack) - k개 
        final_result = "".join(stack[:len(stack) - k])
    else:
        final_result = "".join(stack)
        
    return final_result