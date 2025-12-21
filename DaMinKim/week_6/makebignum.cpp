#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
/*
문제 3: 큰 수 만들기 (Stack / Greedy)
- 각 자리 숫자를 순회하면서 스택의 맨뒤 값이 현재 숫자보다 작고 k > 0 이면 pop 한다.
  (작은 숫자를 제거하여 더 큰 수를 만들기 위함)
- 모두 처리한 뒤에도 k가 남아있으면 뒤에서부터 제거.
- 결과는 스택의 앞부분에서 필요한 만큼을 이어붙인다.
*/
string solution(string number, int k) {
    string st; // 스택 역할을 하는 문자열
    for (char c : number) {
        while (!st.empty() && k > 0 && st.back() < c) {
            st.pop_back();
            k--;
        }
        st.push_back(c);
    }
    // k가 남아있으면 뒤에서부터 제거
    if (k > 0) st.erase(st.size() - k);
    return st;
}

int main() {
    string number;
    int k;
    cout << "number 입력: ";
    cin >> number;

    cout << "k 입력: ";
    cin >> k;

    cout << "결과 = " << solution(number, k) << "\n\n";
}