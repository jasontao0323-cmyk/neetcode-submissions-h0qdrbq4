# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Detect a cycle in a linked list by remembering visited nodes. If a node is revisited, a cycle exists; 
# if the end is reached without repetition, there is no cycle.
# TC: O(n)
# SC: O(n)

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        cur = head
        while cur:
            if cur in seen:
                return True
            seen.add(cur)
            cur = cur.next
        return False