import java.util.*;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        // 캐시 크기가 0이면 모두 miss
        if (cacheSize == 0) {
            return cities.length * 5;
        }

        int time = 0;
        LinkedList<String> cache = new LinkedList<>();

        for (String city : cities) {
            city = city.toLowerCase();

            if (cache.contains(city)) {
                // cache hit
                cache.remove(city);
                cache.addLast(city);
                time += 1;
            } else {
                // cache miss
                if (cache.size() == cacheSize) {
                    cache.removeFirst();
                }
                cache.addLast(city);
                time += 5;
            }
        }

        return time;
    }
}
