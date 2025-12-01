#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
/*
문제 5: 가장 먼 노드 (BFS)
- 그래프를 인접리스트로 만들고 1번에서 BFS 수행하여 각 노드의 최단거리(간선 수)를 구한다.
- 거리의 최댓값을 구하고, 그 거리와 같은 노드의 개수를 반환한다.
*/
int solution(int n, vector<vector<int>> vertex) {
    vector<vector<int>> adj(n + 1);
    for (auto &e : vertex) {
        int a = e[0], b = e[1];
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    vector<int> dist(n + 1, -1);
    queue<int> q;
    dist[1] = 0;
    q.push(1);
    while (!q.empty()) {
        int cur = q.front(); q.pop();
        for (int nx : adj[cur]) {
            if (dist[nx] == -1) {
                dist[nx] = dist[cur] + 1;
                q.push(nx);
            }
        }
    }
    int maxd = 0;
    for (int i = 1; i <= n; ++i) if (dist[i] > maxd) maxd = dist[i];
    int cnt = 0;
    for (int i = 1; i <= n; ++i) if (dist[i] == maxd) cnt++;
    return cnt;
}

int main() {
    int n, m;
    cout << "노드 개수 n 입력: ";
    cin >> n;

    cout << "간선 개수 m 입력: ";
    cin >> m;

    vector<vector<int>> vertex(m, vector<int>(2));
    cout << "간선 목록(a b):\n";
    for (int i = 0; i < m; i++) {
        cin >> vertex[i][0] >> vertex[i][1];
    }

    cout << "결과 = " << solution(n, vertex) << "\n";
}