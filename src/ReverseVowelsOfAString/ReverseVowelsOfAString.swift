/*
345. Reverse Vowels of a String
Solved
Easy
Topics
Companies

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.



Example 1:

Input: s = "hello"
Output: "holle"

Example 2:

Input: s = "leetcode"
Output: "leotcede"

Constraints:

    1 <= s.length <= 3 * 105
    s consist of printable ASCII characters.
* */
class Solution {
    func reverseVowels(_ s: String) -> String {
        let vowels: Set<Character> = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        var sChars = Array(s)
        var left = 0
        var right = sChars.count - 1

        while left < right {
            if vowels.contains(sChars[left]) && vowels.contains(sChars[right]) {
                sChars.swapAt(left, right)
                left += 1
                right -= 1
            }
            if !vowels.contains(sChars[left]) {
                left += 1
            }
            if !vowels.contains(sChars[right]) {
                right -= 1
            }
        }

        return String(sChars)
    }
}
