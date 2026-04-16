# ProductExceptSelf
# TC: O(n^2))
# SC: O(n)
# Logic: Brute force method, compute the product 
# of all other elements by multiplying every value except the one at the current index


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        for i in range(n):
            prod = 1
            for j in range(n):
                if i == j:
                    continue
                prod *= nums[j]

            res[i] = prod
        return res