import java.util.Arrays;

class Solution {

    int[] parent;

    // Find - 루트 찾기 (경로 압축)
    public int find(int x) {
        if(parent[x] == x) return x;
        return parent[x] = find(parent[x]);
    }

    // Union - 두 집합 합치기
    public void union(int a, int b) {
        a = find(a);
        b = find(b);
        if(a != b) parent[b] = a;
    }

    public int solution(int n, int[][] costs) {
        int answer = 0;

        parent = new int[n];
        for(int i = 0; i < n; i++) parent[i] = i;

        // 1. 비용 오름차순 정렬
        Arrays.sort(costs, (a, b) -> a[2] - b[2]);

        // 2. 간선을 하나씩 보면서 MST 만들기
        for(int[] edge : costs) {
            int a = edge[0];
            int b = edge[1];
            int cost = edge[2];

            // 싸이클이 없을 때만 사용
            if(find(a) != find(b)) {
                union(a, b);
                answer += cost;
            }
        }
        return answer;
    }
}
