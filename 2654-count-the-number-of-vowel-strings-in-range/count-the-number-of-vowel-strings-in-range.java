class Solution {
    public int vowelStrings(String[] words, int left, int right) {
        Set<Character> vow = Set.of('a','e','i','o','u');
        int c = 0;
        for(int i = left; i <= right ; i++)
        {
            if(vow.contains(words[i].charAt(0)) && vow.contains(words[i].charAt(words[i].length()-1))){
                c++;
            }
        }       
        return c;
    }
}