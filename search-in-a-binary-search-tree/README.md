# Search in a Binary Search Tree

***

You are given the `root` of a binary search tree (BST) and an integer `val`.

Find the node in the BST that the node's value equals `val` and return the subtree rooted with that node. If such a node does not exist, return `null`.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/12/tree1.jpg)

<pre><code>Input: root = [4,2,7,1,3], val = 2
<strong>Output:
</strong> [2,1,3]</code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/01/12/tree2.jpg)

<pre><code>Input: root = [4,2,7,1,3], val = 5
<strong>Output:
</strong> []</code></pre>

&#x20;

**Constraints:**

* The number of nodes in the tree is in the range `[1, 5000]`.
* `1 <= Node.val <= 107`
* `root` is a binary search tree.
* `1 <= val <= 107`
