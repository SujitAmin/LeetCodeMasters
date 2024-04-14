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

public class Solution {
    // Generates the next lexicographical permutation of the given integer array.
    public void nextPermutation(int[] nums) {
        int firstDecreasingElementIndex = findFirstDecreasing(nums);
        // this is because if it is smaller than zero we reached the last one in this.
        // [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1]
        // so just reverse.
        if (firstDecreasingElementIndex >= 0) {
            //find element just larger than firstDecreasingElementIndex
            int findJustLargerIndex = findJustLargerIndex(nums, firstDecreasingElementIndex);
            swap(nums, firstDecreasingElementIndex, findJustLargerIndex);
        }
        reverse(nums, firstDecreasingElementIndex+1);
    }

    void swap(int[] nums, int firstDecreasingElementIndex, int findJustLargerIndex) {
        int temp = nums[firstDecreasingElementIndex];
        nums[firstDecreasingElementIndex] = nums[findJustLargerIndex];
        nums[findJustLargerIndex] = temp;
    }
    int findFirstDecreasing(int[] nums) {
        for (int i =  nums.length - 1; i > 0; i--) {
            if (nums[i - 1] < nums[i]) {
                return i - 1;
            }
        }
        return -1;
    }

    int findJustLargerIndex(int[] nums, int firstDecreasingElementIndex) {
        for (int i =  nums.length - 1; i > firstDecreasingElementIndex; i--) {
            if (nums[i] > nums[firstDecreasingElementIndex]) {
                return i;
            }
        }
        return firstDecreasingElementIndex;
    }

    void reverse(int[] nums, int i) {
        int j = nums.length - 1;
        while (i <= j) {
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
            i++;
            j--;
        }
    }
}
