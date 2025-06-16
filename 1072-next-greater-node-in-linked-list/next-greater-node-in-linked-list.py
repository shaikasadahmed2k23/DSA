# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        values = []
        answer = []

        while head:
            values.append(head.val)
            answer.append(0)
            head = head.next

        stack = []

        for i in range(len(values)):
            while stack and values[i] > values[stack[-1]]:
                idx = stack.pop()
                answer[idx] = values[i]
            stack.append(i)

        return answer