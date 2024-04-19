/*
415. Add Strings
Solved
Easy
Topics
Companies

Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"

Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"

 

Constraints:

    1 <= num1.length, num2.length <= 104
    num1 and num2 consist of only digits.
    num1 and num2 don't have any leading zeros except for the zero itself.

  
*/

function addStrings(num1, num2) {
    let i = num1.length - 1;
    let j = num2.length - 1;
    let carry = 0;
    let result = [];

    while (i >= 0 || j >= 0 || carry > 0) {
        let num1Value = (i >= 0) ? num1.charCodeAt(i) - '0'.charCodeAt(0) : 0;
        let num2Value = (j >= 0) ? num2.charCodeAt(j) - '0'.charCodeAt(0) : 0;
        let sum = num1Value + num2Value + carry;
        carry = Math.floor(sum / 10);
        result.push(sum % 10);
        i--;
        j--;
    }

    return result.reverse().join('');
}
