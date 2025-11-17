class Solution {
    public void reverseString(char[] s) {
        String r = "";
        int j = 0;
        for(int i = s.length -1 ; i >= (s.length)/2 ; i--)
        {
            // r += s[i];
            char t = s[j];
            s[j] = s[i];
            s[i] = t;
            j++;
        }
        // return r;

    }
}