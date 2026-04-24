# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Recursive linked list reversal involves reversing the rest of the list and fixing the current node’s pointer. The last 
# node becomes the new head, and the original head’s next is set to null.
# TC: O(n)
# SC: O(n)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead