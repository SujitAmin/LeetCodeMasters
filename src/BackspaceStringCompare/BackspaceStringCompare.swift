/*
844. Backspace String Compare
Easy

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
Note that after backspacing an empty text, the text will continue empty.

 

Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".

Constraints:
    1 <= s.length, t.length <= 200
    s and t only contain lowercase letters and '#' characters.

Follow up: Can you solve it in O(n) time and O(1) space?
  
*/

class Solution {
    func backspaceCompare(_ S: String, _ T: String) -> Bool {
        let sChars = Array(S)
        let tChars = Array(T)
        var sIndex = sChars.count - 1
        var tIndex = tChars.count - 1
        var skipS = 0
        var skipT = 0

        while sIndex >= 0 || tIndex >= 0 {
            while sIndex >= 0 {
                if sChars[sIndex] == '#' {
                    skipS += 1
                    sIndex -= 1
                } else if skipS > 0 {
                    skipS -= 1
                    sIndex -= 1
                } else {
                    break
                }
            }
            while tIndex >= 0 {
                if tChars[tIndex] == '#' {
                    skipT += 1
                    tIndex -= 1
                } else if skipT > 0 {
                    skipT -= 1
                    tIndex -= 1
                } else {
                    break
                }
            }
            if (sIndex >= 0 && tIndex >= 0) && sChars[sIndex] != tChars[tIndex] {
                return false
            }
            if (sIndex >= 0) != (tIndex >= 0) {
                return false
            }
            sIndex -= 1
            tIndex -= 1
        }
        return true
    }
}
