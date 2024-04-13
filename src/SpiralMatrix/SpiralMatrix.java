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
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<>();
        int colStart = 0;
        int colEnd = matrix[0].length - 1;
        int rowStart = 0;
        int rowEnd = matrix.length - 1;
        //rowStart <= rowEnd <= made mistake by adding < instead of <=
        while (rowStart <= rowEnd && colStart <= colEnd) {
            for(int i = colStart; i <= colEnd; i++) {
                result.add(matrix[rowStart][i]);
            }
            rowStart++;
            for(int i = rowStart; i <= rowEnd; i++) {
                result.add(matrix[i][colEnd]);
            }
            colEnd--;
            for (int i = colEnd; i >= colStart; i--) {
                // to avoid repetition.
                if (rowStart <= rowEnd) {
                    result.add(matrix[rowEnd][i]);
                }
            }
            rowEnd--;
            for(int i = rowEnd; i >= rowStart; i--) {
                // to avoid repetition.
                if (colStart <= colEnd) {
                    result.add(matrix[i][colStart]);
                }
            }
            colStart++;
        }
        return result;
    }
}