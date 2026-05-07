# To find the k closest points to the origin, compare points by their 
# squared distance from the origin, avoiding unnecessary computation.
# TC:O(nlogn)
# SC:O(1) or O(n)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda p: p[0]**2 + p[1]**2)
        return points[:k]