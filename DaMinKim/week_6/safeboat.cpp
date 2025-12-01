#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

/*
문제 2: 구명보트 (Two pointers, Greedy)
- 사람들을 오름차순 정렬한다.
- 가장 가벼운(left)와 가장 무거운(right)를 비교하여 같이 탈 수 있으면 둘 다 태우고,
  아니면 무거운 사람만 태운다. (right--)
- 이 과정을 모든 사람이 처리될 때까지 반복한다.
*/
int solution(vector<int> people, int limit) {
    sort(people.begin(), people.end());
    int left = 0, right = (int)people.size() - 1;
    int boats = 0;
    while (left <= right) {
        if (left == right) { // 한 사람 남음
            boats++;
            break;
        }
        if (people[left] + people[right] <= limit) {
            left++; right--; // 두 명 태움
        } else {
            right--; // 한 명(무거운 사람)만 태움
        }
        boats++;
    }
    return boats;
}

int main() {
    int peopleCnt, limit;
    cout << "people 개수: ";
    cin >> peopleCnt;

    vector<int> people(peopleCnt);
    cout << "people 목록: ";
    for (int i = 0; i < peopleCnt; i++) cin >> people[i];

    cout << "limit: ";
    cin >> limit;

    cout << "결과 = " << solution(people, limit) << "\n\n";
}