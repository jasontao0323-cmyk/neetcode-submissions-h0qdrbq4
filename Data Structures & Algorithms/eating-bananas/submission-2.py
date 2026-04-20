# minEatingSpeed
# Binary search is used to find 
# the smallest eating speed that allows finishing the piles within h hours.
# TC: O(n*logm)
# SC: O(1)

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res