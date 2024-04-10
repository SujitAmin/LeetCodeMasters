/*
You are given an array of integers nums. Return the length of the longest
subarray of nums which is either strictly increasing or strictly decreasing.



Example 1:
Input: nums = [1,4,3,3,2]

Output: 2

Explanation:

The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].

The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].

Hence, we return 2.

Example 2:

Input: nums = [3,3,3,3]

Output: 1

Explanation:

The strictly increasing subarrays of nums are [3], [3], [3], and [3].

The strictly decreasing subarrays of nums are [3], [3], [3], and [3].

Hence, we return 1.

Example 3:

Input: nums = [3,2,1]

Output: 3

Explanation:

The strictly increasing subarrays of nums are [3], [2], and [1].

The strictly decreasing subarrays of nums are [3], [2], [1], [3,2], [2,1], and [3,2,1].

Hence, we return 3.
Constraints:
    1 <= nums.length <= 50
    1 <= nums[i] <= 50
 */
class Solution {
    func longestMonotonicSubarray(_ nums: [Int]) -> Int {
        if nums.count == 1 {
            return 1
        }

        var increasingLength = 1
        var decreasingLength = 1
        var result = 1;

        for i in 1..<nums.count {
            if nums[i] > nums[i - 1] {
                increasingLength = increasingLength + 1
            } else {
                increasingLength = 1 // Reset if not strictly increasing
            }

            if nums[i] < nums[i - 1] {
                decreasingLength = decreasingLength + 1
            } else {
                decreasingLength = 1 // Reset if not strictly decreasing
            }
            // you forgot to check this. we need to check for every iteration.
            result = max(result, max(increasingLength, decreasingLength));
        }

        return result; // Use Swift's max function
    }
}