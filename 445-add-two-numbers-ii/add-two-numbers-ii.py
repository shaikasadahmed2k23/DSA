# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        temp2 = l2
        # while tem1:
        r1 = []
        r2 = []
        while temp1:
            r1.append(temp1.val)
            temp1 = temp1.next
        # print(r1)

        while temp2:
            r2.append(temp2.val)
            temp2 = temp2.next
        # print(r2)
        
        # x = sum(r1) + sum(r2)
        x1 = ''.join(map(str, r1))
        x2 = ''.join(map(str, r2))

        x3 = str(int(x1) + int(x2))
        # print(x3)
        head = ListNode(int(x3[0]))  
        current = head
        for i in range(1, len(x3)): 
            current.next = ListNode(int(x3[i]))
            current = current.next
        
        return head