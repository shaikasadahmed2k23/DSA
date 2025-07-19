from typing import List

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()  # Sorting helps make parent folders come before subfolders
        hm = {}  # To store valid parent folders
        ln = [len(f) for f in folder]  # Precompute lengths
        n = len(folder)
        result = []
        idx = 0  # Index to track current element

        while idx < n:
            curr = folder[idx]
            # Check if any prefix of this folder already exists in hm
            flag = False
            temp = ""
            for i in range(1, len(curr)):
                if curr[i] == '/':
                    temp = curr[:i]
                    if temp in hm:
                        flag = True
                        break

            if not flag:
                hm[curr] = 1
                result.append(curr)

            idx += 1

        return result
