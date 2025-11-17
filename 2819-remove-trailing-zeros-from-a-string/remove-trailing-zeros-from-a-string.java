import java.util.*;
class Solution {
    public String removeTrailingZeros(String num) {
        String r = "";
        int n = num.length();
        int c=0;
        for(int i = n - 1; i >= 0 ; i--)
        {
            if(num.charAt(i) != '0')
            {
                c = i;
                // break;
                int j = 0;
                while(j<=c)
                {
                    r += num.charAt(j);
                    j++;
                }
                break;
            }
        }              
        // System.out.print(c);
        // StringBuilder sb = StringBuilder(r);
        // String sb1 = sb.reverse().toString();
        return r;
        // for(int i = 0)
    }
}