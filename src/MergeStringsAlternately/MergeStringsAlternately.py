'''
1768. Merge Strings Alternately
Easy

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.

Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s

Example 3:
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d

Constraints:
    1 <= word1.length, word2.length <= 100
    word1 and word2 consist of lowercase English letters.

  
'''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Using a list to build strings for better performance in Python
        result = []
        m = len(word1)
        n = len(word2)
        i = 0
        # Loop until we reach the end of at least one string
        while i < m or i < n:
            # If we have not reached the end of word1, add the character to result
            if i < m:
                result.append(word1[i])
            # If we have not reached the end of word2, add the character to result
            if i < n:
                result.append(word2[i])
            i += 1
        # Join all characters in the list to form the final string
        return ''.join(result)
