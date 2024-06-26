/*
* 1302. Deepest Leaves Sum
Medium
Given the root of a binary tree, return the sum of values of its deepest leaves.

Example 1:
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15

Example 2:
Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19

Constraints:
    The number of nodes in the tree is in the range [1, 104].
    1 <= Node.val <= 100
* */
class Solution {
    public int deepestLeavesSum(TreeNode root) {
        if (root == null) {
            return 0;
        }
        if (root.left == null && root.right == null) {
            return root.val;
        }

        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        int result = 0;

        while(!queue.isEmpty()) {
            int size = queue.size();
            int count = 0;
            int sum = 0;
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                if (node.left == null && node.right == null) {
                    count++;
                    sum += node.val;
                }
                if (node.left != null)
                    queue.add(node.left);

                if (node.right != null)
                    queue.add(node.right);
            }
            if (count == size) {
                result = sum;
            }
        }
        return result;

    }
}