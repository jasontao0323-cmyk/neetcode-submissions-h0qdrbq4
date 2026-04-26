# findDuplicate
# Sorting the array brings duplicates together, 
# allowing for a single scan to find the first duplicate.
# O(nlogn)
# O(1)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]
        return -1