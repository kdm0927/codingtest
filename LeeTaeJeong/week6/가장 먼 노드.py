from collections import deque

def solution(n, vertex):
    # 노드 번호가 1부터 시작하므로 n+1 크기로 리스트를 초기화
    graph = [[] for _ in range(n + 1)]
    for a, b in vertex:
        # 양방향 간선 추가
        graph[a].append(b)
        graph[b].append(a)

    # distances[i]는 1번 노드에서 i번 노드까지의 최단 거리를 의미
    # 거리를 -1로 초기화하여 방문하지 않은 노드를 표시
    distances = [-1] * (n + 1)
    
    # BFS 실행
    queue = deque([1])  # 시작 노드를 큐에 추가
    distances[1] = 0    # 시작 노드의 거리는 0

    while queue:
        current_node = queue.popleft()
        current_distance = distances[current_node]
        
        # 현재 노드와 연결된 모든 인접 노드 탐색
        for neighbor in graph[current_node]:
            # 아직 방문하지 않은 노드라면 (거리가 -1이라면)
            if distances[neighbor] == -1:
                # 최단 거리를 업데이트하고 큐에 추가
                distances[neighbor] = current_distance + 1
                queue.append(neighbor)

    max_distance = max(distances)
    
    # max_distance와 같은 거리를 가진 노드의 개수를 세어 반환
    # distances[1:]을 사용하여 1번 노드부터 n번 노드까지의 거리만 확인
    return distances.count(max_distance)