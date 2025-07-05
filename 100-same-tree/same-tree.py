# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def Inorder(self,root,res):
    #     if root:
    #         self.Inorder(root.left,res)
    #         res.append(root.val)
    #         self.Inorder(root.right,res)
    #     return res
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # res1 = []
        # x = self.Inorder(p,res1)
        # res2 = []
        # y = self.Inorder(q,res2)
        # # print(x,y)
        # if len(x) != len(y):
        #     return False
        
        # for i in range(len(x)):
            # if x[i] != y[i]:
        #         return False
        
        # return True
