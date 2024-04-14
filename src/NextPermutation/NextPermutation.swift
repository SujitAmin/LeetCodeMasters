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
    // Generates the next lexicographical permutation of the given integer array.
    func nextPermutation(_ nums: inout [Int]) {
        let firstDecreasingElementIndex = findFirstDecreasing(nums)
        // this is because if it is smaller than zero we reached the last one in this.
        // [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]
        // so just reverse.
        if firstDecreasingElementIndex >= 0 {
            // find element just larger than firstDecreasingElementIndex
            let findJustLargerIndex = self.findJustLargerIndex(nums, firstDecreasingElementIndex)
            swap(&nums, firstDecreasingElementIndex, findJustLargerIndex)
        }
        reverse(&nums, firstDecreasingElementIndex + 1)
    }

    func swap(_ nums: inout [Int], _ firstDecreasingElementIndex: Int, _ findJustLargerIndex: Int) {
        let temp = nums[firstDecreasingElementIndex]
        nums[firstDecreasingElementIndex] = nums[findJustLargerIndex]
        nums[findJustLargerIndex] = temp
    }

    func findFirstDecreasing(_ nums: [Int]) -> Int {
        for i in stride(from: nums.count - 1, through: 1, by: -1) {
            if nums[i - 1] < nums[i] {
                return i - 1
            }
        }
        return -1
    }

    func findJustLargerIndex(_ nums: [Int], _ firstDecreasingElementIndex: Int) -> Int {
        for i in stride(from: nums.count - 1, through: firstDecreasingElementIndex + 1, by: -1) {
            if nums[i] > nums[firstDecreasingElementIndex] {
                return i
            }
        }
        return firstDecreasingElementIndex
    }

    func reverse(_ nums: inout [Int], _ start: Int) {
        var i = start
        var j = nums.count - 1
        while i < j {
            let temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i += 1
            j -= 1
        }
    }
}
