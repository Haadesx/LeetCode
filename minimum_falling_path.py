# Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

# A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

 

# Example 1:


# Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
# Output: 13
# Explanation: There are two falling paths with a minimum sum as shown.
# Example 2:


# Input: matrix = [[-19,57],[-40,-5]]
# Output: -59
# Explanation: The falling path with a minimum sum is shown.



class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix)
        
        # Traverse the matrix starting from the second row
        for row in range(1, n):
            for col in range(n):
                # For each element, add the minimum value from the possible previous row elements
                min_above = matrix[row-1][col]
                if col > 0:
                    min_above = min(min_above, matrix[row-1][col-1])
                if col < n - 1:
                    min_above = min(min_above, matrix[row-1][col+1])
                matrix[row][col] += min_above
        
        # The result is the minimum value in the last row
        return min(matrix[-1])

