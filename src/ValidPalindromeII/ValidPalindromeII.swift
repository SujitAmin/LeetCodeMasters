/*
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


    
*/

import Foundation

class Solution {
    func validPalindrome(_ str: String) -> Bool {
        let chars = Array(str)
        var left = 0
        var right = chars.count - 1

        while left < right {
            if chars[left] == chars[right] {
                left += 1
                right -= 1
            } else {
                return isPalindrome(chars, left + 1, right) || isPalindrome(chars, left, right - 1)
            }
        }
        return true
    }

    private func isPalindrome(_ chars: [Character], _ left: Int, _ right: Int) -> Bool {
        var left = left
        var right = right

        while left < right {
            if chars[left] == chars[right] {
                left += 1
                right -= 1
            } else {
                return false
            }
        }
        return true
    }
}
