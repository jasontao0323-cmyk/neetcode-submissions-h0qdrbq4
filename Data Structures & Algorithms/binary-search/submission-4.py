# Search 
# Binary search is a divide-and-conquer algorithm that 
# efficiently finds a target value in a sorted array. 
# It works by repeatedly dividing the search range in half and comparing the middle 
# element to the target. The time complexity of binary search is 
# O(log n), making it significantly faster than linear search for large datasets.
# TC: O(logn)
# SC: O(logn)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            m = l + ((r - l) // 2)
            if nums[m] >= target:
                r = m
            elif nums[m] < target:
                l = m + 1
        return l if (l < len(nums) and nums[l] == target) else -1