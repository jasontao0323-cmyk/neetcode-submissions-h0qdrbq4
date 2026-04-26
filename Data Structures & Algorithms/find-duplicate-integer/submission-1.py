# findDuplicate
# Fast And Slow Pointers
# Floyd’s Fast & Slow Pointer technique identifies the 
# duplicate number in an array by treating it as a linked list with a cycle.
# Sorting the array brings duplicates together, 
# allowing for a single scan to find the first duplicate.
# O(n)
# O(1)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow