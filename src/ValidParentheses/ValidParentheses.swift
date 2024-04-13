/*
   242. Valid Anagram
Solved
Easy
Topics
Companies

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

 

Constraints:

    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.

 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

    
*/

class Solution {
    func isValid(_ s: String) -> Bool {
        let map: [Character: Character] = [")": "(", "]": "[", "}": "{"]
        var stack = [Character]()

        for ch in s {
            if let match = map[ch] {
                if !stack.isEmpty && stack.last == match {
                    stack.removeLast()
                } else {
                    return false
                }
            } else {
                stack.append(ch)
            }
        }
        return stack.isEmpty
    }
}
