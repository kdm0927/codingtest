import java.util.*;

class Solution {
    public int solution(String str1, String str2) {
        Map<String, Integer> map1 = makeMultiSet(str1);
        Map<String, Integer> map2 = makeMultiSet(str2);

        int intersection = 0;
        int union = 0;

        Set<String> keys = new HashSet<>();
        keys.addAll(map1.keySet());
        keys.addAll(map2.keySet());

        for (String key : keys) {
            int cnt1 = map1.getOrDefault(key, 0);
            int cnt2 = map2.getOrDefault(key, 0);

            intersection += Math.min(cnt1, cnt2);
            union += Math.max(cnt1, cnt2);
        }

        if (union == 0) {
            return 65536;
        }

        return (int) ((double) intersection / union * 65536);
    }

    private Map<String, Integer> makeMultiSet(String str) {
        Map<String, Integer> map = new HashMap<>();
        str = str.toLowerCase();

        for (int i = 0; i < str.length() - 1; i++) {
            char c1 = str.charAt(i);
            char c2 = str.charAt(i + 1);

            if (Character.isLetter(c1) && Character.isLetter(c2)) {
                String key = "" + c1 + c2;
                map.put(key, map.getOrDefault(key, 0) + 1);
            }
        }
        return map;
    }
}
