# 113. Path Sum II

## Medium

***

Given the `root` of a binary tree and an integer `targetSum`, return _all **root-to-leaf** paths where the sum of the node values in the path equals_ `targetSum`_. Each path should be returned as a list of the node **values**, not node references_.

A **root-to-leaf** path is a path starting from the root and ending at any leaf node. A **leaf** is a node with no children.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/18/pathsumii1.jpg)

<pre><code>Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
<strong>Output:
</strong> [[5,4,11,2],[5,8,4,5]]
<strong>Explanation:
</strong> There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22</code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg)

<pre><code>Input: root = [1,2,3], targetSum = 5
<strong>Output:
</strong> []</code></pre>

**Example 3:**

<pre><code>Input: root = [1,2], targetSum = 0
<strong>Output:
</strong> []</code></pre>

&#x20;

**Constraints:**

* The number of nodes in the tree is in the range `[0, 5000]`.
* `-1000 <= Node.val <= 1000`
* `-1000 <= targetSum <= 1000`
