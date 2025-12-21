import java.util.*;

class Solution {
    static class Stage {
        int number;
        double failureRate;

        Stage(int number, double failureRate) {
            this.number = number;
            this.failureRate = failureRate;
        }
    }

    public int[] solution(int N, int[] stages) {
        int[] count = new int[N + 2];

        // 각 스테이지에 머물러 있는 사람 수
        for (int stage : stages) {
            count[stage]++;
        }

        int totalPlayers = stages.length;
        List<Stage> list = new ArrayList<>();

        // 실패율 계산
        for (int i = 1; i <= N; i++) {
            double failureRate;

            if (totalPlayers == 0) {
                failureRate = 0;
            } else {
                failureRate = (double) count[i] / totalPlayers;
            }

            list.add(new Stage(i, failureRate));
            totalPlayers -= count[i];
        }

        // 정렬
        Collections.sort(list, (a, b) -> {
            if (Double.compare(b.failureRate, a.failureRate) != 0) {
                return Double.compare(b.failureRate, a.failureRate);
            }
            return Integer.compare(a.number, b.number);
        });

        // 결과 추출
        int[] answer = new int[N];
        for (int i = 0; i < N; i++) {
            answer[i] = list.get(i).number;
        }

        return answer;
    }
}
