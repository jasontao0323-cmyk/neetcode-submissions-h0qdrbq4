# searchMatrix 
# The text discusses four methods for searching a 2D matrix: linear scan, 
# staircase search, binary search, and a one-pass binary search. 
# Each method is explained with its intuition, algorithm, and time and space complexity. 
# The one-pass binary search leverages the sorted 
# nature of the matrix to perform a single binary search across the entire matrix.
# TC: O(log(m*n))
# SC: O(1)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS * COLS - 1
        while l <= r:
            m = l + (r - l) // 2
            row, col = m // COLS, m % COLS
            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True
        return False