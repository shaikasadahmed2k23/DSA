class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """

        if target == "z":
            return letters[0]
        nn = len(letters)
        st = set()
        for i in range(nn):
            st.add(letters[i])
        # print(st)
        # return 'x'
        flag1 = False
        for i in range(ord('a'), ord('z') + 1):
            if chr(i) > target and chr(i) in st:
                flag1 = True
                break

        if flag1:
            return chr(i)
        else:
            return letters[0]