# Two Pointers
# TC: O(n)
# SC: O(1)
# Brute Force: Try every possible pair of lines and compute the area they form.

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) - 1
        res = 0
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res

