def solution(n, costs):
    answer = 0
    
    # 1. 비용을 기준으로 오름차순 정렬 (가장 적은 비용의 다리부터 고려하기 위함)
    costs.sort(key=lambda x: x[2])
    
    # 각 섬의 부모 노드를 저장할 리스트 (처음에는 자기 자신이 부모)
    parent = [i for i in range(n)]
    
    # 부모 노드를 찾는 함수 (Find)
    def find(target):
        if parent[target] != target:
            parent[target] = find(parent[target]) # 경로 압축 (Path Compression)
        return parent[target]
    
    # 두 섬을 연결하는 함수 (Union)
    def union(a, b):
        rootA = find(a)
        rootB = find(b)
        if rootA < rootB:
            parent[rootB] = rootA
        else:
            parent[rootA] = rootB

    edges_count = 0 # 연결된 다리의 개수
    
    for u, v, cost in costs:
        # 2. 두 섬의 부모가 다르면(즉, 아직 연결되지 않았다면) 다리를 건설
        if find(u) != find(v):
            union(u, v)
            answer += cost
            edges_count += 1
            
            # MST의 간선 개수는 항상 n-1개입니다. 다 찾았으면 종료.
            if edges_count == n - 1:
                break
                
    return answer