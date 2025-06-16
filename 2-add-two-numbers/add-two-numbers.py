class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy_head = ListNode(0)
        current = dummy_head

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         t1 = l1
#         t2 = l2
#         # li1 = li2 = []
#         s1 = ""
#         c1 = 0
#         while t1:
#             s1 += str(t1.val)
#             # li1.append(t1.val)
#             c1 += 1
#             t1 = t1.next
#         s2 = ""
#         c2 = 0
#         while t2:
#             s2 += str(t2.val)
#             # li2.append(t2.val)
#             c2 += 1 
#             t2 = t2.next  
#         # print(s1)
#         s1 = int(s1)
#         s2 = int(s2)
#         # print(s1+s2)
#         xx = str(s1+s2)
#         xx = xx[::-1]
#         # print(xx)
#         dummy_head = ListNode(0)
#         current = dummy_head
#         xx = list(xx)
#         for i in xx:
#             dummy_head.val = i
#             dummy_head = dummy_head.next
#         return dummy_head
#         print(xx)
#         # if c1>c2:
#         #     t3 = l1
#         #     i = 0
#         #     while(t3 and i<len(xx)):
#         #         t3.val = int(xx[i])
#         #         t3 = t3.next
#         #         i+=1
#         #     return l1
#         # else:
#         #     t3 = l2
#         #     i = 0
#         #     while(t3 and i<len(xx)):
#         #         t3.val = int(xx[i])
#         #         t3 = t3.next
#         #         i+=1
#         #     return l2
        
        
#         # # print(xx[::-1])
#         # # print(s2)   
#         # # print()   
#         # # return l1

        