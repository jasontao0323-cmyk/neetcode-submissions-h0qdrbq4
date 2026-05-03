# Generate permutations by building them from smaller permutations. Insert the 
# first number into every possible position of all smaller permutations.
# TC: O(n!*n^2)
# SC: O(n!*n)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        perms = self.permute(nums[1:])
        res = []
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        return res 
        