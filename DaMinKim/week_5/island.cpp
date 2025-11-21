// 탐욕법(그리디)으로 푼 "섬 연결하기" 문제
// Kruskal 알고리즘을 사용하여 최소 신장 트리(MST)의 비용을 구합니다.
//
// 사용법(프로그램 실행 후 입력):
// 1) 섬의 개수 n (정수, 예: 4)
// 2) 비용 정보의 개수 m (정수, 예: 5)
// 3) m개의 줄에 걸쳐: a b cost (각 줄은 공백으로 구분된 세 정수)
//    (a와 b는 섬 번호, 0~n-1 범위, cost는 비용)
// 예시 입력(문제 예시):
// 4
// 5
// 0 1 1
// 0 2 2
// 1 2 5
// 1 3 1
// 2 3 8
// 출력: 최소 비용(예: 4)

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// 유니온-파인드(Disjoint Set) 구현
struct UnionFind {
	vector<int> parent;
	vector<int> rankv;
	UnionFind(int n) : parent(n), rankv(n, 0) {
		for (int i = 0; i < n; ++i) parent[i] = i;
	}
	int find(int x) {
		if (parent[x] == x) return x;
		return parent[x] = find(parent[x]);
	}
	bool unite(int a, int b) {
		a = find(a); b = find(b);
		if (a == b) return false;
		if (rankv[a] < rankv[b]) swap(a,b);
		parent[b] = a;
		if (rankv[a] == rankv[b]) rankv[a]++;
		return true;
	}
};

// 간선 구조체
struct Edge {
	int u, v, w;
};

// solution: Kruskal로 MST 비용 계산
int solution(int n, const vector<Edge>& edges) {
	// 간선들을 가중치 오름차순으로 정렬
	vector<Edge> es = edges;
	sort(es.begin(), es.end(), [](const Edge& a, const Edge& b){ return a.w < b.w; });

	UnionFind uf(n);
	int total = 0;
	int used = 0; // 사용한 간선 수
	for (const auto& e : es) {
		if (uf.unite(e.u, e.v)) {
			total += e.w;
			used++;
			if (used == n - 1) break; // 모든 섬을 연결했으면 종료
		}
	}
	return total;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int n;
	cout << "섬의 개수 n을 입력하세요: ";
	if (!(cin >> n)) return 0;
	int m;
	cout << "비용 정보 개수 m을 입력하세요: ";
	cin >> m;
	vector<Edge> edges;
	cout << "각 줄마다: a b cost (0부터 n-1 사이의 섬 번호)\n";
	for (int i = 0; i < m; ++i) {
		int a, b, c;
		cin >> a >> b >> c;
		edges.push_back({a, b, c});
	}
	int ans = solution(n, edges);
	cout << "최소 비용: " << ans << '\n';
	return 0;
}

