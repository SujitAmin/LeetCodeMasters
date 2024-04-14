'''
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
  
'''

class Solution:
    def next_permutation(self, nums):
        first_decreasing_element_index = self.find_first_decreasing(nums)
        # this is because if it is smaller than zero we reached the last one in this.
        # [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1]
        # so just reverse.
        if first_decreasing_element_index >= 0:
            # find element just larger than firstDecreasingElementIndex
            find_just_larger_index = self.find_just_larger_index(nums, first_decreasing_element_index)
            self.swap(nums, first_decreasing_element_index, find_just_larger_index)
        self.reverse(nums, first_decreasing_element_index + 1)

    def swap(self, nums, first_decreasing_element_index, find_just_larger_index):
        nums[first_decreasing_element_index], nums[find_just_larger_index] = nums[find_just_larger_index], nums[first_decreasing_element_index]

    def find_first_decreasing(self, nums):
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                return i - 1
        return -1

    def find_just_larger_index(self, nums, first_decreasing_element_index):
        for i in range(len(nums) - 1, first_decreasing_element_index, -1):
            if nums[i] > nums[first_decreasing_element_index]:
                return i
        return first_decreasing_element_index

    def reverse(self, nums, i):
        j = len(nums) - 1
        while i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
