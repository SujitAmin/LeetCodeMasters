/*
42. Trapping Rain Water
Solved
Hard
Topics
Companies
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
    n == height.length
    1 <= n <= 2 * 104
    0 <= height[i] <= 105
  
*/

class Solution {
    func trap(_ height: [Int]) -> Int {
        var left = 0
        var right = height.count - 1
        // we can store water in the pointer if the leftmax is greater than current height.
        var leftMax = 0
        var rightMax = 0
        var result = 0

        while left <= right {
            // we want to maximize height so if the current height is less than move pointer.
            if height[left] <= height[right] {
                if leftMax <= height[left] {
                    leftMax = max(leftMax, height[left])
                } else {
                    result += leftMax - height[left]
                }
                left += 1
            } else if height[left] >= height[right] {
                if rightMax <= height[right] {
                    rightMax = max(rightMax, height[right])
                } else {
                    result += rightMax - height[right]
                }
                right -= 1
            }
        }
        return result
    }
}