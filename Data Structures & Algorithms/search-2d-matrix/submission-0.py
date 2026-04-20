# searchMatrix 
# Brute Force: Brute 
# force approach checks every matrix element sequentially, ignoring sorted structure.
# TC: O(m*n)
# SC: O(1)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == target:
                    return True
        return False
        