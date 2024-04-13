# /*
# 345. Reverse Vowels of a String
# Solved
# Easy
# Topics
# Companies
#
# Given a string s, reverse only all the vowels in the string and return it.
#
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
#
#
#
# Example 1:
#
# Input: s = "hello"
# Output: "holle"
#
# Example 2:
#
# Input: s = "leetcode"
# Output: "leotcede"
#
# Constraints:
#
# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.
# * */
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        s_list = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            if s_list[left] in vowels and s_list[right] in vowels:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
            if s_list[left] not in vowels:
                left += 1
            if s_list[right] not in vowels:
                right -= 1

        return ''.join(s_list)
