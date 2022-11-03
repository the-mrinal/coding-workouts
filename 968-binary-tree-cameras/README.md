# 968. Binary Tree Cameras

## Hard

***

You are given the `root` of a binary tree. We install cameras on the tree nodes where each camera at a node can monitor its parent, itself, and its immediate children.

Return _the minimum number of cameras needed to monitor all nodes of the tree_.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/12/29/bst\_cameras\_01.png)

<pre><code>Input: root = [0,0,null,0,0]
<strong>Output:
</strong> 1
<strong>Explanation:
</strong> One camera is enough to monitor all nodes if placed as shown.</code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2018/12/29/bst\_cameras\_02.png)

<pre><code>Input: root = [0,0,null,0,null,0,null,null,0]
<strong>Output:
</strong> 2
<strong>Explanation:
</strong> At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.</code></pre>

&#x20;

**Constraints:**

* The number of nodes in the tree is in the range `[1, 1000]`.
* `Node.val == 0`
