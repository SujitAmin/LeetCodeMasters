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
    func isAnagram(_ s: String, _ t: String) -> Bool {
        if s.count != t.count {
            return false
        }

        var table = Array(repeating: 0, count: 26) // Array to store letter counts
        let aScalarValue = Int("a".unicodeScalars.first!.value) // Unicode scalar value of 'a'

        for char in s.unicodeScalars {
            table[Int(char.value) - aScalarValue] += 1
        }

        for char in t.unicodeScalars {
            let index = Int(char.value) - aScalarValue
            table[index] -= 1
            if table[index] < 0 {
                return false
            }
        }
        return true
    }
}
