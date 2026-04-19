# largestReactangleArea
# A monotonic stack is used to determine the maximum width of the shortest bar in each 
# rectangle. The stack maintains increasing bar heights, and when a shorter bar 
# is encountered, the top of the stack is popped and processed, ensuring optimal and clean computation.
# O(n^2)
# O(1)

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        stack = []

        for i in range(n + 1):
            while stack and (i == n  or heights[stack[-1]] >= heights[i]):
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            stack.append(i)
        return maxArea