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
