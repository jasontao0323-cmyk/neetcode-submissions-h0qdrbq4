# Sorting a list of values after each insertion to find the k-th 
# largest number is simple but inefficient.
# TC: O(m*nlogn)
# SC: O(m) extra space, O(1) O(n) space depending on the sorting algorithm


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.arr = nums

    def add(self, val: int) -> int:
        self.arr.append(val)
        self.arr.sort()
        return self.arr[len(self.arr) - self.k]
