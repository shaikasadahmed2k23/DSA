class Solution(object):
    def isPalindrome(self, s):
        l = 0
        h = len(s) - 1

        while l < h:
            if not s[l].isalnum():
                l += 1
                continue

            if not s[h].isalnum():
                h -= 1
                continue

            if s[l].lower() != s[h].lower():
                return False

            l += 1
            h -= 1

        return True

                
        # s1 = ""
        # for i in s:
        #     # print(i)
        #     if i.isalnum():
        #         s1 += i.lower()
        # # # print(s1)
        # s2 = s1[::-1]
        # # if s1 == s1[::-1]:
        # #     return True
        # # else:
        # #     return False
        # l = 0
        # h = len(s1) - 1
        # for i in range(len(s2)//2):
        #     if s2[l] != s2[h]:
        #         return False
        #     l += 1
        #     h -= 1
        # return True