# 105. Construct Binary Tree from Preorder and Inorder Traversal

## Medium

***

Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return _the binary tree_.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/tree.jpg)

<pre><code>Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
<strong>Output:
</strong> [3,9,20,null,null,15,7]</code></pre>

**Example 2:**

<pre><code>Input: preorder = [-1], inorder = [-1]
<strong>Output:
</strong> [-1]</code></pre>

&#x20;

**Constraints:**

* `1 <= preorder.length <= 3000`
* `inorder.length == preorder.length`
* `-3000 <= preorder[i], inorder[i] <= 3000`
* `preorder` and `inorder` consist of **unique** values.
* Each value of `inorder` also appears in `preorder`.
* `preorder` is **guaranteed** to be the preorder traversal of the tree.
* `inorder` is **guaranteed** to be the inorder traversal of the tree.
