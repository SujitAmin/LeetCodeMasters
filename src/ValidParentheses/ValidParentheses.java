/*
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


*/

class Solution {
    public boolean isValid(String s) {
        HashMap<Character,Character> map = new HashMap<>();
        map.put(')','(');
        map.put(']','[');
        map.put('}','{');
        Stack<Character> stack = new Stack<>();
        for(int i=0; i<s.length() ; i++){
            char ch = s.charAt(i);
            // opening parentheses add to the stack.
            if(!map.containsKey(ch)){
                stack.push(ch);
            }
            else if(!stack.isEmpty() && map.get(ch) == stack.peek()){
                stack.pop();
            } else {
                return false;
            }
        }
        return stack.isEmpty();
    }
}
