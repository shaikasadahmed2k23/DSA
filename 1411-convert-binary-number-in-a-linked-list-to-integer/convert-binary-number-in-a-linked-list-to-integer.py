# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        t = head
        s = ""
        while(t):
            s = s + str(t.val)
            t = t.next
        return int(s,2)
                