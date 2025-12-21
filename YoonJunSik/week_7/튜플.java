import java.util.*;

class Solution {
    public int[] solution(String s) {
        // 바깥 {{ }}
        s = s.substring(2, s.length() - 2);

        // 집합 분리
        String[] parts = s.split("\\},\\{");

        List<List<Integer>> sets = new ArrayList<>();

        for (String part : parts) {
            String[] nums = part.split(",");
            List<Integer> list = new ArrayList<>();
            for (String num : nums) {
                list.add(Integer.parseInt(num));
            }
            sets.add(list);
        }

        // 원소 개수 기준 정렬
        sets.sort(Comparator.comparingInt(List::size));

        // 튜플 복원
        List<Integer> result = new ArrayList<>();
        Set<Integer> used = new HashSet<>();

        for (List<Integer> set : sets) {
            for (int num : set) {
                if (!used.contains(num)) {
                    result.add(num);
                    used.add(num);
                    break;
                }
            }
        }

        // 배열로 변환
        return result.stream().mapToInt(i -> i).toArray();
    }
}
