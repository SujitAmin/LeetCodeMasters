'''
    680. Valid Palindrome II
    Solved
    Easy
    Topics
    Companies
    
    Given a string s, return true if the s can be palindrome after deleting at most one character from it.
    
     
    
    Example 1:
    
    Input: s = "aba"
    Output: true
    
    Example 2:
    
    Input: s = "abca"
    Output: true
    Explanation: You could delete the character 'c'.
    
    Example 3:
    
    Input: s = "abc"
    Output: false
    
     
    
    Constraints:
    
        1 <= s.length <= 105
        s consists of lowercase English letters.


    
'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return self.isPalindrome(s, left + 1, right) or self.isPalindrome(s, left, right - 1)
        return True

    def isPalindrome(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
