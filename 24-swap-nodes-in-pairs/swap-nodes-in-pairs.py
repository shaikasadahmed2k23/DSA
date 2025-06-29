# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         t = head
#         c = 0
#         while t:
#             if t.next != None:
#                 temp = t.val
#                 t.val = t.next.val
#                 t.next.val = temp
#         return head
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t = head
        while t and t.next:
            t.val, t.next.val = t.next.val, t.val
            t = t.next.next  
        return head