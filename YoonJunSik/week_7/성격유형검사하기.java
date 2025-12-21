import java.util.*;

class Solution {
    public String solution(String[] survey, int[] choices) {
        Map<Character, Integer> score = new HashMap<>();

        // 모든 성격 유형 점수 0으로 초기화
        char[] types = {'R','T','C','F','J','M','A','N'};
        for (char c : types) {
            score.put(c, 0);
        }

        // 질문별 점수 누적
        for (int i = 0; i < survey.length; i++) {
            char disagree = survey[i].charAt(0);
            char agree = survey[i].charAt(1);
            int choice = choices[i];

            int point = Math.abs(choice - 4);

            if (choice < 4) {
                score.put(disagree, score.get(disagree) + point);
            } else if (choice > 4) {
                score.put(agree, score.get(agree) + point);
            }
        }

        // 지표별 결과 생성
        StringBuilder result = new StringBuilder();

        result.append(selectType(score, 'R', 'T'));
        result.append(selectType(score, 'C', 'F'));
        result.append(selectType(score, 'J', 'M'));
        result.append(selectType(score, 'A', 'N'));

        return result.toString();
    }

    private char selectType(Map<Character, Integer> score, char a, char b) {
        if (score.get(a) > score.get(b)) return a;
        if (score.get(a) < score.get(b)) return b;
        return a < b ? a : b; // 점수 같으면 사전순
    }
}
