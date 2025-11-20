import java.util.Arrays;

class Solution {
    public int solution(int[] d, int budget) {
        //부서 신청 금액 오름차순 정렬
        Arrays.sort(d);

        int count = 0;
        int sum = 0;

        //작은 금액부터 더해가며 갯수를 세기
        for(int money : d)
        {
            if(sum + money > budget) // 예산 초과의 경우
            {
                break;
            }
            sum += money;
            count++;
        }
        return count;
    }
}
