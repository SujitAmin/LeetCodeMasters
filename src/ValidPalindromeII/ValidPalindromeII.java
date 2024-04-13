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

class Solution {
    public boolean validPalindrome(String str) {
        int left = 0;
        int right = str.length() - 1;

        while( left < right) {
            if (str.charAt(left) == str.charAt(right)) {
                left++;
                right--;
            } else {
                return isPalindrome(str, left + 1, right) || isPalindrome(str, left , right - 1);
            }
        }
        return true;
    }
    private boolean isPalindrome(String str, int left, int right) {
        while(left < right) {
            if (str.charAt(left) == str.charAt(right)) {
                left++;
                right--;
            } else {
                return false;
            }
        }
        return true;
    }
}