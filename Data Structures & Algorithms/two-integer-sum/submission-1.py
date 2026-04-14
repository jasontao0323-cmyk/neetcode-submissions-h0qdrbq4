# Two_Sum
# Hashmap
# TC: O(n) 
# SC: O(n)
# Logic: use hashmap to store the value and index of each element, then interate to check 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}  # val -> index

        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        return []