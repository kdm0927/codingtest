from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n + 1)] 
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    visited = [-1] * (n + 1) # 거리 저장용 (-1은 미방문)
    visited[1] = 0           # 출발점 거리는 0
    queue = deque([1])       # 큐 생성 및 시작점 삽입
    

    while queue:
        current_node = queue.popleft()
        
        for neighbor in graph[current_node]:
            if visited[neighbor] == -1:      
                visited[neighbor] = visited[current_node] + 1 
                queue.append(neighbor)  
    

    max_distance = max(visited) # 가장 멀리 떨어진 거리 찾기
    return visited.count(max_distance) # 그 거리를 가진 노드 개수 세기