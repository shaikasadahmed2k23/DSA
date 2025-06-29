class Solution {
    public int fib(int n) {
        if(n <= 1) return n;
        int l = fib(n-1);
        int sl = fib(n-2);
        return l+sl;
    }
    // public int fn(int n){
    //     if(n <= 1) return n;
    //     int l = fn(n-1);
    //     int sl = fn(n-2);
    //     return l+sl;
    // }
}