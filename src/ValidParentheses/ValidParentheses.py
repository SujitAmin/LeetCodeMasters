'''
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

    
'''

class Solution:
    def isValid(self, s: str) -> bool:
        # Map to hold the corresponding opening brackets for each closing bracket
        bracket_map = {')': '(', ']': '[', '}': '{'}

        # Stack to keep track of opening brackets
        stack = []

        # Iterate over each character in the string
        for char in s:
            # If the character is not a closing bracket, push to stack
            if char not in bracket_map:
                stack.append(char)
            # If it's a closing bracket, check if the stack is not empty and top matches the bracket
            elif stack and stack[-1] == bracket_map[char]:
                stack.pop()
            else:
                return False

        # If stack is empty, all brackets are matched properly
        return not stack
