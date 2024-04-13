/*
* 125. Valid Palindrome
Solved
Easy
Topics
Companies

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.



Constraints:

    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.


* */
class Solution {
    func isPalindrome(_ s: String) -> Bool {
        let chars = Array(s.lowercased()) // Convert string to lowercase character array for easier access
        var left = 0
        var right = chars.count - 1
        
        while left < right {
            // Skip non-alphanumeric characters by advancing left index
            while left < right && !chars[left].isLetter && !chars[left].isNumber {
                left += 1
            }
            // Skip non-alphanumeric characters by decreasing right index
            while left < right && !chars[right].isLetter && !chars[right].isNumber {
                right -= 1
            }
            
            // Compare characters
            if chars[left] != chars[right] {
                return false
            }
            
            left += 1
            right -= 1
        }
        
        return true
    }
}
