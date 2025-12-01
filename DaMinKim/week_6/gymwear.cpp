#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

/*
문제 1: 체육복 (Greedy)
- lost와 reserve에 중복(도난당한 학생이 여벌을 가진 경우)이 있을 수 있으므로
  먼저 중복을 제거한다.
- 이후 여벌을 가진 학생을 순회하면서 앞번호, 뒷번호에게 빌려줄 수 있는지 확인한다.
- 최종 가능한 학생 수 = n - (빌려주지 못한 lost 의 수)
*/
int solution(int n, vector<int> lost, vector<int> reserve) {
    // 정렬해두면 탐색이 쉽다
    sort(lost.begin(), lost.end());
    sort(reserve.begin(), reserve.end());

    // 중복 처리: lost 와 reserve 둘 다에 있는 학생은 자기 체육복으로 사용 (빌려줄 수 없음)
    vector<int> real_lost, real_reserve;
    // 투 포인터로 중복 제거
    int i = 0, j = 0;
    while (i < (int)lost.size() && j < (int)reserve.size()) {
        if (lost[i] == reserve[j]) {
            // 중복인 경우: 둘 다 제거(도난당했지만 여벌로 사용)
            i++; j++;
        } else if (lost[i] < reserve[j]) {
            real_lost.push_back(lost[i++]);
        } else {
            real_reserve.push_back(reserve[j++]);
        }
    }
    while (i < (int)lost.size()) real_lost.push_back(lost[i++]);
    while (j < (int)reserve.size()) real_reserve.push_back(reserve[j++]);

    // 빌려주기 시도: 각 여벌 학생이 앞 또는 뒤에게 빌려준다
    vector<bool> hasLost(real_lost.size(), true); // true = 아직 빌리지 못한 상태
    for (int r : real_reserve) {
        for (int idx = 0; idx < (int)real_lost.size(); ++idx) {
            if (!hasLost[idx]) continue; // 이미 해결된 lost
            if (abs(real_lost[idx] - r) == 1) {
                hasLost[idx] = false; // 빌려줌
                break;
            }
        }
    }
    int remaining = 0;
    for (bool b : hasLost) if (b) remaining++;
    return n - remaining;
}

int main() {
    int n;
    cout << "n 입력: ";
    cin >> n;

    int lostCnt, reserveCnt;
    cout << "lost 개수: ";
    cin >> lostCnt;

    vector<int> lost(lostCnt);
    cout << "lost 목록: ";
    for (int i = 0; i < lostCnt; i++) cin >> lost[i];

    cout << "reserve 개수: ";
    cin >> reserveCnt;

    vector<int> reserve(reserveCnt);
    cout << "reserve 목록: ";
    for (int i = 0; i < reserveCnt; i++) cin >> reserve[i];

    cout << "결과 = " << solution(n, lost, reserve) << "\n\n";
}