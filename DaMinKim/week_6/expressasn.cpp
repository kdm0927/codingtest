#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>
using namespace std;

/*
문제 4: N으로 표현 (DP - 집합 사용)
- 1~8번까지 N을 i번 이어붙인 숫자(예: N=5, i=3 => 555)를 기본으로 집합에 넣는다.
- DP[i] = i번 N을 사용해서 만들 수 있는 모든 숫자의 집합.
- DP[i]를 만들 때 j=1..i-1 로 분해하여 DP[j]와 DP[i-j] 의 모든 조합에 +,-,*,/ 연산을 적용.
- number가 어떤 DP[i]에 나타나면 i를 반환. (i<=8)
- 범위를 제한하지 않으면 집합이 커질 수 있으므로 실무에선 값의 절대값을 적당히 제한하기도 한다.
*/
int solution(int N, int number) {
    if (N == number) return 1;
    vector<unordered_set<int>> dp(9); // dp[1]..dp[8]
    int concatenated = 0;
    for (int i = 1; i <= 8; ++i) {
        concatenated = concatenated * 10 + N; // NNN...
        dp[i].insert(concatenated); // 예: 5, 55, 555 ...
    }

    for (int i = 1; i <= 8; ++i) {
        // 이미 concatenated 수로 해결 가능하면 반환
        if (dp[i].count(number)) return i;
        for (int j = 1; j < i; ++j) {
            for (int a : dp[j]) {
                for (int b : dp[i - j]) {
                    dp[i].insert(a + b);
                    dp[i].insert(a - b);
                    dp[i].insert(a * b);
                    if (b != 0) dp[i].insert(a / b);
                }
            }
        }
        if (dp[i].count(number)) return i;
    }
    return -1;
}

int main() {
        int N, numberTarget;
    cout << "N과 number 입력: ";
    cin >> N >> numberTarget;

    cout << "결과 = " << solution(N, numberTarget) << "\n\n";
}