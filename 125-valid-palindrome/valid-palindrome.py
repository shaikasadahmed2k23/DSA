class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""
        for i in range(len(s)):
            if s[i].isalnum():
                s1 += s[i].lower()
        print(s1)
        return s1 == s1[::-1]