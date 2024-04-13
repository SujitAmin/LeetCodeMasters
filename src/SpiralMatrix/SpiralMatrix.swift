/*
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
  
*/
class Solution {
    func spiralOrder(_ matrix: [[Int]]) -> [Int] {
        var result = [Int]()
        var colStart = 0
        var colEnd = matrix[0].count - 1
        var rowStart = 0
        var rowEnd = matrix.count - 1
        // rowStart <= rowEnd <= made mistake by adding < instead of <=
        while rowStart <= rowEnd && colStart <= colEnd {
            for i in colStart...colEnd {
                result.append(matrix[rowStart][i])
            }
            rowStart += 1
            for i in rowStart...rowEnd {
                result.append(matrix[i][colEnd])
            }
            colEnd -= 1
            if rowStart <= rowEnd { // moved condition outside the loop
                for i in stride(from: colEnd, through: colStart, by: -1) {
                    result.append(matrix[rowEnd][i])
                }
            }
            rowEnd -= 1
            if colStart <= colEnd { // moved condition outside the loop
                for i in stride(from: rowEnd, through: rowStart, by: -1) {
                    result.append(matrix[i][colStart])
                }
            }
            colStart += 1
        }
        return result
    }
}
