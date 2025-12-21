def solution(n, costs):
    answer = 0
    
    costs.sort(key=lambda x: x[2])
    
    parent = [i for i in range(n)]

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(a,b):
        root_a = find(a)
        root_b = find(b)
        
        if root_a < root_b:
            parent[root_b] = root_a
        else:
            parent[root_a] = root_b
    
    edges = 0
    for i, j, cost in costs:
        if find(i) != find(j):
            union(i,j)
            answer += cost
            edges += 1
            
            if edges == n-1:
                break
    return answer