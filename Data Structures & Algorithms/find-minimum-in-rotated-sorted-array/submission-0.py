# findmin
# Brute Force: Rotated sorted arrays contain all original values, shifted. The simplest way to 
# find the minimum is to look at every element and pick the smallest one.
# TC: O(n)
# SC: O(1)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)