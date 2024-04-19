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

func addStrings(_ num1: String, _ num2: String) -> String {
        let chs1: [Character] = Array(num1).reversed()
        let chs2: [Character] = Array(num2).reversed()
        var isOne = 0
        var res = [Character]()
        var i = 0
        var j = 0

        while i < chs1.count || j < chs2.count || isOne == 1 {
            let c1 = i < chs1.count ? Int(String(chs1[i]))! : 0
            let c2 = j < chs2.count ? Int(String(chs2[j]))! : 0

            let s = (c1 + c2 + isOne) % 10
            isOne = (c1 + c2 + isOne) / 10
            i += 1
            j += 1
            res.append(Character(String(s)))
        }
        return String(res.reversed())
}