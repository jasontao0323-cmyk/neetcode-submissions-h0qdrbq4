# largestReactangleArea
# For each bar, treat it as the shortest in the rectangle, find the widest rectangle 
# it can form, and repeat for all bars to find the maximum rectangle.
# O(n^2)
# O(1)

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0

        for i in range(n):
            height = heights[i]

            rightMost = i + 1
            while rightMost < n and heights[rightMost] >= height:
                rightMost += 1

            leftMost = i
            while leftMost >= 0 and heights[leftMost] >= height:
                leftMost -= 1

            rightMost -= 1
            leftMost += 1
            maxArea = max(maxArea, height * (rightMost - leftMost + 1))
        return maxArea
        