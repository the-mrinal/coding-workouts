# 103. Binary Tree Zigzag Level Order Traversal

## Medium

***

Given the `root` of a binary tree, return _the zigzag level order traversal of its nodes' values_. (i.e., from left to right, then right to left for the next level and alternate between).

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)

<pre><code>Input: root = [3,9,20,null,null,15,7]
<strong>Output:
</strong> [[3],[20,9],[15,7]]</code></pre>

**Example 2:**

<pre><code>Input: root = [1]
<strong>Output:
</strong> [[1]]</code></pre>

**Example 3:**

<pre><code>Input: root = []
<strong>Output:
</strong> []</code></pre>

&#x20;

**Constraints:**

* The number of nodes in the tree is in the range `[0, 2000]`.
* `-100 <= Node.val <= 100`
