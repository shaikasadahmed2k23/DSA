from typing import List

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()  
        print(folder)
        hm = {}  
        ln = [len(f) for f in folder]  
        n = len(folder)
        result = []
        idx = 0  

        while idx < n:
            curr = folder[idx]
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
