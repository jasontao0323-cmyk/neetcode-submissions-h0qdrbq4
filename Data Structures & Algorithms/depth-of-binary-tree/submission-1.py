# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Recursive DFS calculates binary tree depth by exploring all nodes. Depth equals 1 plus the maximum 
# depth of left and right subtrees, with None nodes having a depth of 0.
# TC: O(n)
# SC: O(h)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))