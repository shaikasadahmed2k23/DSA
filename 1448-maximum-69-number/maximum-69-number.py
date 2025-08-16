class Solution:
    def maximum69Number (self, num: int) -> int:
        res = []
        n1 = list(str(num))  # Convert to list to make it mutable
        for i in range(len(n1)):
            original = n1[i]
            if original == '6':
                n1[i] = '9'  # Change 6 to 9
                res.append(int(''.join(n1)))
                n1[i] = original  # revert back for next iteration
            elif original == '9':
                n1[i] = '6'  # Change 9 to 6
                res.append(int(''.join(n1)))
                n1[i] = original  # revert back
        res.append(num)  # Also consider original number
        return max(res)
