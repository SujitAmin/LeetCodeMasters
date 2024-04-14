'''
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
  
'''

class Solution:
    def backspaceCompare(self, S, T):
        sIndex = len(S) - 1
        tIndex = len(T) - 1
        skipS = 0
        skipT = 0

        while sIndex >= 0 or tIndex >= 0:
            # Process backspaces in S
            while sIndex >= 0:
                if S[sIndex] == '#':
                    skipS += 1
                    sIndex -= 1
                elif skipS > 0:
                    skipS -= 1
                    sIndex -= 1
                else:
                    break
            # Process backspaces in T
            while tIndex >= 0:
                if T[tIndex] == '#':
                    skipT += 1
                    tIndex -= 1
                elif skipT > 0:
                    skipT -= 1
                    tIndex -= 1
                else:
                    break
            # Compare characters from S and T
            if (sIndex >= 0 and tIndex >= 0) and S[sIndex] != T[tIndex]:
                return False
            # If one is at end and the other isn't, return False
            if (sIndex >= 0) != (tIndex >= 0):
                return False
            sIndex -= 1
            tIndex -= 1
        return True
