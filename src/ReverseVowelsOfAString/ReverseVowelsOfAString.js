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
function reverseVowels(s)   {
    const vowels = new Set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']);
    const sChars = Array.from(s); // Convert string to array to mutate characters
    let left = 0;
    let right = s.length - 1;

    while (left < right) {
        if (vowels.has(sChars[left]) && vowels.has(sChars[right])) {
            // Swap characters when both are vowels
            const temp = sChars[left];
            sChars[left] = sChars[right];
            sChars[right] = temp;
            left++;
            right--;
        }
        if (!vowels.has(sChars[left])) {
            left++;
        }
        if (!vowels.has(sChars[right])) {
            right--;
        }
    }
    // Convert array back to string
    return sChars.join('');
}
