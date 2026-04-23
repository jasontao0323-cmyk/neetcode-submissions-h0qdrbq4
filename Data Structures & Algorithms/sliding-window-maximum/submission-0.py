# maxSlidingWindow
# A sliding window approach is used to find the maximum value in 
# each window of size k, but it is inefficient due to repeated scanning.
# TC: O(n*k)
# SC: O(1) extra space, O(n-k+1) space for the output array

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []

        for i in range(len(nums) - k + 1):
            maxi = nums[i]
            for j in range(i, i + k):
                maxi = max(maxi, nums[j])
            output.append(maxi)

        return output