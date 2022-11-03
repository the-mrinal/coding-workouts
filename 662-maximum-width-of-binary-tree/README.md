# 662. Maximum Width of Binary Tree

## Medium

***

Given the `root` of a binary tree, return _the **maximum width** of the given tree_.

The **maximum width** of a tree is the maximum **width** among all levels.

The **width** of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is **guaranteed** that the answer will in the range of a **32-bit** signed integer.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/05/03/width1-tree.jpg)

<pre><code>Input: root = [1,3,2,5,3,null,9]
<strong>Output:
</strong> 4
<strong>Explanation:
</strong> The maximum width exists in the third level with length 4 (5,3,null,9).</code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2022/03/14/maximum-width-of-binary-tree-v3.jpg)

<pre><code>Input: root = [1,3,2,5,null,null,9,6,null,7]
<strong>Output:
</strong> 7
<strong>Explanation:
</strong> The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).</code></pre>

**Example 3:**

![](https://assets.leetcode.com/uploads/2021/05/03/width3-tree.jpg)

<pre><code>Input: root = [1,3,2,5]
<strong>Output:
</strong> 2
<strong>Explanation:
</strong> The maximum width exists in the second level with length 2 (3,2).</code></pre>

&#x20;

**Constraints:**

* The number of nodes in the tree is in the range `[1, 3000]`.
* `-100 <= Node.val <= 100`
