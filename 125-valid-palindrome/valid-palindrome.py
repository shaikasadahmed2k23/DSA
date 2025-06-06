class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""
        for i in s:
            if i.isalnum():
                s1 = s1 + i
        # print(s1)
        s1 = s1.lower()
        # print(s1)
        if s1 == s1[::-1]:
            return True
        else:
            return False
