# Search
# Linear search checks each array element sequentially for a target value.
# TC: O(n)
# SC: O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1