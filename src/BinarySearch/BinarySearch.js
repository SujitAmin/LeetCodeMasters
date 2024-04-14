/*
704. Binary Search
Solved
Easy
Topics
Companies

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Constraints:
    1 <= nums.length <= 104
    -104 < nums[i], target < 104
    All the integers in nums are unique.
    nums is sorted in ascending order.
  
*/

var search = (nums, target) => {
    var left = 0;
    var right = nums.length - 1;
    while (left <= right) {
        // Calculating middle index
        var mid = Math.floor((left + right) / 2);
        if (nums[mid] === target) {
            // Target value found
            return mid;
        } else if (nums[mid] < target) {
            // Continue searching to the right
            left = mid + 1;
        } else {
            // Continue searching to the left
            right = mid - 1;
        }
    }
    // Target not found
    return -1;
};
