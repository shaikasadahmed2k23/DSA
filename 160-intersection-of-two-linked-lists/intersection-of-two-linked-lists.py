# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        c1 = c2 = 0
        temp1 = headA
        temp2 = headB
        while temp1:
            if temp1:
                c1 += 1
                temp1 = temp1.next
        print(c1)
        while temp2:
            if temp2:
                c2 += 1
                temp2 = temp2.next
        print(c2)

        x = abs(c1-c2)
        f = 0
        if c1 > c2:
            f = 1
        else:
            f = 2
        tempA1 = headA
        tempB1 = headB
        if f == 1:
            while x > 0:
                tempA1 = tempA1.next
                x -= 1
        else:
            while x > 0:
                tempB1 = tempB1.next
                x -= 1
        while tempA1:
            if tempA1 == tempB1:
                return tempA1
            # else:
            tempA1 = tempA1.next
            tempB1 = tempB1.next
            

        # return headA