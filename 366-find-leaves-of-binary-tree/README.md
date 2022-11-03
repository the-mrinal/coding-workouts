# 366. Find Leaves of Binary Tree

## Medium

***

Given the `root` of a binary tree, collect a tree's nodes as if you were doing this:

* Collect all the leaf nodes.
* Remove all the leaf nodes.
* Repeat until the tree is empty.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/16/remleaves-tree.jpg)

<pre><code>Input: root = [1,2,3,4,5]
<strong>Output:
</strong> [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.</code></pre>

**Example 2:**

<pre><code>Input: root = [1]
<strong>Output:
</strong> [[1]]</code></pre>

&#x20;

**Constraints:**

* The number of nodes in the tree is in the range `[1, 100]`.
* `-100 <= Node.val <= 100`
