/*
문제 설명
조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA

조이스틱을 각 방향으로 움직이면 아래와 같습니다.

▲ - 다음 알파벳
▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
▶ - 커서를 오른쪽으로 이동 (마지막 위치에서 오른쪽으로 이동하면 첫 번째 문자에 커서)
예를 들어 아래의 방법으로 "JAZ"를 만들 수 있습니다.

- 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
- 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
- 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.

제한 사항
name은 알파벳 대문자로만 이루어져 있습니다.
name의 길이는 1 이상 20 이하입니다.
입출력 예
name	return
"JEROEN"	56
"JAN"	23
*/

#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

// 조이스틱 문제: 주어진 name을 만들기 위해 필요한 최소 조작 횟수를 구한다.
// 수직 이동(알파벳 변경)은 각 자리별로 min(ch - 'A', 'Z' - ch + 1)
// 수평 이동(커서 이동)의 최적값은 연속된 'A' 구간을 피하는 방식으로 계산.

int solution(const string& name) {
	int n = static_cast<int>(name.size());
	int vertical = 0;
	for (char c : name) {
		vertical += min(c - 'A', 'Z' - c + 1);
	}
	int move = n - 1; // 최악: 오른쪽으로만 이동
	for (int i = 0; i < n; ++i) {
		int j = i + 1;
		while (j < n && name[j] == 'A') ++j;
		// i까지 가서, 뒤의 A구간을 건너뛰고 끝에서 돌아오는 방식 고려
		move = min(move, i + n - j + min(i, n - j));
	}
	return vertical + move;
}

int main() {
	string name;
	cout << "이름을 대문자로 입력하세요 (예: JEROEN): ";
	cin >> name;
	cout << "최소 조작 횟수: " << solution(name) << '\n';
	return 0;
}
