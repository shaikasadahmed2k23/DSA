import java.util.HashMap;

public class Solution {
    public int longestPalindrome(String s) {
        HashMap<Character, Integer> countMap = new HashMap<>();
        for (char c : s.toCharArray()) {
            countMap.put(c, countMap.getOrDefault(c, 0) + 1);
        }
        
        int length = 0;
        boolean oddFound = false;
        
        for (int count : countMap.values()) {
            length += (count / 2) * 2;
            if (count % 2 == 1) {
                oddFound = true;
            }
        }
        
        if (oddFound) {
            length += 1;
        }
        
        return length;
    }
}
