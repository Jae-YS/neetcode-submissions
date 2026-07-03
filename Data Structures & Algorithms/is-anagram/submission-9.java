class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        Map<Character, Integer> countMap1 = new HashMap<>();
        Map<Character, Integer> countMap2 = new HashMap<>();

        for (int i = 0; i < s.length(); i++){
            char c1 = s.charAt(i);
            char c2 = t.charAt(i);

            countMap1.put(c1, countMap1.getOrDefault(c1, 0) + 1);
            countMap2.put(c2, countMap2.getOrDefault(c2, 0) + 1);
        }

        return countMap1.equals(countMap2);
    }
}

