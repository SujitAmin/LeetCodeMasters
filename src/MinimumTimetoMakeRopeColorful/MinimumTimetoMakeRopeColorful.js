/*
1578. Minimum Time to Make Rope Colorful
Solved
Medium
Topics
Companies
Hint

Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.

Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.

Return the minimum time Bob needs to make the rope colorful.

 

Example 1:

Input: colors = "abaac", neededTime = [1,2,3,4,5]
Output: 3
Explanation: In the above image, 'a' is blue, 'b' is red, and 'c' is green.
Bob can remove the blue balloon at index 2. This takes 3 seconds.
There are no longer two consecutive balloons of the same color. Total time = 3.

Example 2:

Input: colors = "abc", neededTime = [1,2,3]
Output: 0
Explanation: The rope is already colorful. Bob does not need to remove any balloons from the rope.

Example 3:

Input: colors = "aabaa", neededTime = [1,2,3,4,1]
Output: 2
Explanation: Bob will remove the balloons at indices 0 and 4. Each balloons takes 1 second to remove.
There are no longer two consecutive balloons of the same color. Total time = 1 + 1 = 2.

Constraints:
    n == colors.length == neededTime.length
    1 <= n <= 105
    1 <= neededTime[i] <= 104
    colors contains only lowercase English letters.
  
*/

var minCost = (colors, neededTime) => {
    var totalTime = 0;
    // Initialize two pointers i, j.
    var i = 0, j = 0;
    while (i < neededTime.length && j < neededTime.length) {
        var currentTotal = 0;
        var currentMax = 0;
        // Find all the balloons having the same color as the
        // balloon indexed at i, record the total removal time
        // and the maximum removal time.
        while (j < neededTime.length && colors.charAt(i) === colors.charAt(j)) {
            currentTotal += neededTime[j];
            currentMax = Math.max(currentMax, neededTime[j]);
            j++;
        }
        // Once we reach the end of the current group, add the cost of
        // this group to total_time, and reset two pointers.
        totalTime += currentTotal - currentMax;
        i = j;
    }
    return totalTime;
};
