'''
20. Valid Parentheses
Solved
Easy
Topics
Companies
Hint

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Constraints:
    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.
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
