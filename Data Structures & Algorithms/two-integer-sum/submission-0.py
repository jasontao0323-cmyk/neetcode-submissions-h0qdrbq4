# Two_Sum
# Brute Force
# TC: O(n^2) 
# SC: O(1)
# Logic: Add two numbers one by one 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []