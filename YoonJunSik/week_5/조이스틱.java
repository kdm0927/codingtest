class Solution {
    public int solution(String name) {
        int len = name.length();
        int answer = 0;

        // 1. 상하 이동 최소 횟수
        for(int i = 0; i < len; i++) {
            char c = name.charAt(i);
            int up = c - 'A';
            int down = 'Z' - c + 1;
            answer += Math.min(up, down);
        }

        // 2. 좌우 이동 최소 횟수
        int move = len - 1; // 기본 직진 이동

        for(int i = 0; i < len; i++)
        {
            int next = i + 1;

            // A가 연속되는 구간을 찾기
            while(next < len && name.charAt(next) == 'A') {
                next++;
            }

            // 되돌아가기 방식 중 최소값으로 갱신
            move = Math.min(move, i * 2 + (len - next)); // 오른쪽 → 왼쪽 돌아오기
            move = Math.min(move, (len - next) * 2 + i); // 왼쪽 → 오른쪽 돌아오기
        }
        answer += move;
        return answer;
    }
}
