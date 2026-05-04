# Iterative method builds subsets, avoiding duplicates by 
# sorting the array and using two indices to control subset generation.
# TC: O(n*2^n)
# SC: O(1) for extra space, O(2^n) space for the outpost list

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def backtrack(i, subset):
            if i == len(nums):
                res.add(tuple(subset))
                return

            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            backtrack(i + 1, subset)

        nums.sort()
        backtrack(0, [])
        return [list(s) for s in res]