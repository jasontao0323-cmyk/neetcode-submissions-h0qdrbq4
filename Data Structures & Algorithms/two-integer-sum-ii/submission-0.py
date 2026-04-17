# Two Sum
# Brute Force ignores the ordering and simply checks every possible pair.
# TC: O(n^2)
# SC: O(1)


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        return []