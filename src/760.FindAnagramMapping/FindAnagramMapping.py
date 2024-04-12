# /*
# * 760. Find Anagram Mappings
# Easy
#
# You are given two integer arrays nums1 and nums2 where nums2 is an anagram of nums1. Both arrays may contain duplicates.
# Return an index mapping array mapping from nums1 to nums2 where mapping[i] = j means the ith element in nums1 appears in nums2 at index j. If there are multiple answers, return any of them.
# An array a is an anagram of an array b means b is made by randomizing the order of the elements in a.
# Example 1:
# Input: nums1 = [12,28,46,32,50], nums2 = [50,12,32,46,28]
# Output: [1,4,3,2,0]
# Explanation: As mapping[0] = 1 because the 0th element of nums1 appears at nums2[1], and mapping[1] = 4 because the 1st element of nums1 appears at nums2[4], and so on.
#
# Example 2:
# Input: nums1 = [84,46], nums2 = [84,46]
# Output: [0,1]
#
# Constraints:
#     1 <= nums1.length <= 100
#     nums2.length == nums1.length
#     0 <= nums1[i], nums2[i] <= 105
#     nums2 is an anagram of nums1.
# * */
from typing import List

class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_to_index = {}
        # Build a map from element to its index in nums2
        for index, num in enumerate(nums2):
            num_to_index[num] = index

        # Build the result list by mapping each element of nums1 to its index in nums2
        result = [num_to_index[num] for num in nums1]
        return result