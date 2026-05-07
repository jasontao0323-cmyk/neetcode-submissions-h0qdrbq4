# Sorting the array reveals the k-th largest element at index n-k.
# TC: O(nlogn)
# SC: O(1)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]