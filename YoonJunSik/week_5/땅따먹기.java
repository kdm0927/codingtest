class Solution {
    int solution(int[][] land) {
        int n = land.length;

        // 각 행을 위에서 계산된 최대 점수로 갱신해서 사용
        for(int i = 1; i < n; i++)
        {
            land[i][0] += Math.max(Math.max(land[i-1][1], land[i-1][2]), land[i-1][3]);
            land[i][1] += Math.max(Math.max(land[i-1][0], land[i-1][2]), land[i-1][3]);
            land[i][2] += Math.max(Math.max(land[i-1][0], land[i-1][1]), land[i-1][3]);
            land[i][3] += Math.max(Math.max(land[i-1][0], land[i-1][1]), land[i-1][2]);
        }

        // 마지막 행에서 가장 큰 값이 정답
        int last = land[n-1][0];
        last = Math.max(last, land[n-1][1]);
        last = Math.max(last, land[n-1][2]);
        last = Math.max(last, land[n-1][3]);

        return last;
    }
}