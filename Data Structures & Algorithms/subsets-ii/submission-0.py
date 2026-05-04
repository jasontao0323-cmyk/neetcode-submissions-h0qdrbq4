# Brute-force subset generation avoids duplicates by sorting the array, storing 
# subsets as tuples in a set, and converting the set back to a list.
# TC: O(n*2^n)
# SC: O(2^n)

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