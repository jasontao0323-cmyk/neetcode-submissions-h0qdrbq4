# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Reverse nodes in groups of k by checking if the current segment has at least k nodes. If so, recursively 
# reverse the rest of the list and then reverse the current group.
# TC: O(n)
# SC: O(n/k)

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        group = 0
        while cur and group < k:
            cur = cur.next
            group += 1

        if group == k:
            cur = self.reverseKGroup(cur, k)
            while group > 0:
                tmp = head.next
                head.next = cur
                cur = head
                head = tmp
                group -= 1
            head = cur
        return head