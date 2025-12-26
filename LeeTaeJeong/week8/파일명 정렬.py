import re

def solution(files):
    # 정렬의 기준이 되는 키(Key)를 생성하는 함수
    def sort_key(filename):
        # 정규표현식을 사용하여 HEAD, NUMBER, TAIL 분리
        match = re.match(r'(\D+)(\d{1,5})(.*)', filename)
        
        if match:
            head = match.group(1)
            number = match.group(2)
            # tail = match.group(3) # 정렬 조건에 TAIL은 포함되지 않음
            
            # 튜플을 반환하면 앞의 요소부터 순차적으로 비교하여 정렬함
            return (head.lower(), int(number))
            
    return sorted(files, key=sort_key)