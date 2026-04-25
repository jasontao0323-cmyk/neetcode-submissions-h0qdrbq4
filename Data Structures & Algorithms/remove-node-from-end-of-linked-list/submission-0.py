# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Brute Force: Nodes are stored in an array for direct access to the nth node from the end, 
# allowing for easy deletion by adjusting the previous node’s next pointer.
# TC: O(N)
# SC: O(N)

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        removeIndex = len(nodes) - n
        if removeIndex == 0:
            return head.next

        nodes[removeIndex - 1].next = nodes[removeIndex].next
        return head