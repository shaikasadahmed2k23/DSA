# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        curr = head
        curr2 = head
        lar = []
        rar = []
        c = 0
        ans = []
        fa = []
        while curr:
            d = curr.val
            if d < x:
                lar.append(d)
            elif d == x:
                c += 1
            else:
                rar.append(d)
            curr = curr.next
            ans.append(d)
        # print(lar,rar,c) #([1, 2, 2], [4, 5], 1)
        fa.extend(lar)
        # print(fa)
        n = len(lar)
        m = len(ans)
        # for j in range(n,m):
            # fa.append
        for i in ans:
            if i >= x:
                fa.append(i)
        print(fa)
        idx = 0
        while curr2:
            curr2.val = fa[idx]
            idx += 1
            curr2 = curr2.next
        return head