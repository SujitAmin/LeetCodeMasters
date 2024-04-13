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

var spiralOrder = (matrix) => {
    let result = [];
    let colStart = 0;
    let colEnd = matrix[0].length - 1;
    let rowStart = 0;
    let rowEnd = matrix.length - 1;

    // rowStart <= rowEnd <= made mistake by adding < instead of <=
    while (rowStart <= rowEnd && colStart <= colEnd) {
        for (let i = colStart; i <= colEnd; i++) {
            result.push(matrix[rowStart][i]);
        }
        rowStart++;
        for (let i = rowStart; i <= rowEnd; i++) {
            result.push(matrix[i][colEnd]);
        }
        colEnd--;
        for (let i = colEnd; i >= colStart; i--) {
            // to avoid repetition.
            if (rowStart <= rowEnd) {
                result.push(matrix[rowEnd][i]);
            }
        }
        rowEnd--;
        for (let i = rowEnd; i >= rowStart; i--) {
            // to avoid repetition.
            if (colStart <= colEnd) {
                result.push(matrix[i][colStart]);
            }
        }
        colStart++;
    }
    return result;
};
