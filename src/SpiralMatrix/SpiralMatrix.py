'''
    54. Spiral Matrix
Solved
Medium
Topics
Companies
Hint

Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

 

Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 10
    -100 <= matrix[i][j] <= 100
  
'''

def spiral_order(matrix):
    result = []
    col_start = 0
    col_end = len(matrix[0]) - 1
    row_start = 0
    row_end = len(matrix) - 1
    # rowStart <= rowEnd <= made mistake by adding < instead of <=
    while row_start <= row_end and col_start <= col_end:
        for i in range(col_start, col_end + 1):
            result.append(matrix[row_start][i])
        row_start += 1
        for i in range(row_start, row_end + 1):
            result.append(matrix[i][col_end])
        col_end -= 1
        for i in range(col_end, col_start - 1, -1):
            # to avoid repetition.
            if row_start <= row_end:
                result.append(matrix[row_end][i])
        row_end -= 1
        for i in range(row_end, row_start - 1, -1):
            # to avoid repetition.
            if col_start <= col_end:
                result.append(matrix[i][col_start])
        col_start += 1
    return result
