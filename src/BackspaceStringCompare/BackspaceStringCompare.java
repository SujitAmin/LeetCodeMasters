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
    public boolean backspaceCompare(String S, String T) {
        int sIndex = S.length() - 1;
        int tIndex = T.length() - 1;
        int skipS = 0;
        int skipT = 0;

        while( sIndex >= 0 || tIndex >= 0) {
            while (sIndex >= 0) {
                if (S.charAt(sIndex) == '#') {
                    skipS++;
                    sIndex--;
                } else if (skipS > 0) {
                    skipS--;
                    sIndex--;
                } else {
                    break;
                }
            }
            while (tIndex >= 0) {
                if (T.charAt(tIndex) == '#') {
                    skipT++;
                    tIndex--;
                } else if (skipT > 0) {
                    skipT--;
                    tIndex--;
                } else {
                    break;
                }
            }
            if ((sIndex >= 0 && tIndex >= 0 ) && S.charAt(sIndex) != T.charAt(tIndex)) {
                return false;
            }
            if ((sIndex >= 0) != (tIndex >= 0)) {
                return false;
            }
            sIndex--;
            tIndex--;
        }
        return true;
    }
}