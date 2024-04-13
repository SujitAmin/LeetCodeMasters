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
    public String reverseVowels(String s) {
        Set<Character> set = new HashSet<>();
        char[] sChar = s.toCharArray();
        // ignore the upeer case character.
        set.addAll(Arrays.asList('a','e','i','o','u', 'A','E','I','O','U'));
        int left = 0;
        int right = s.length() - 1; // forgot this previously.
        while (left < right) {
            if (set.contains(s.charAt(left)) && set.contains(s.charAt(right))) {
                char character = sChar[left];
                sChar[left] = sChar[right]; // notice this.
                sChar[right] = character;
                left++;
                right--;
            }
            if (!set.contains(s.charAt(left))) {
                left++;
            }
            if (!set.contains(s.charAt(right))) {
                right--;
            }
        }
        // Converting char array back to String
        return new String(sChar); // notice this.
    }
}