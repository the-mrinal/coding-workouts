# Same Tree

***

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg)

<pre><code>Input: p = [1,2,3], q = [1,2,3]
<strong>Output:
</strong> true</code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg)

<pre><code>Input: p = [1,2], q = [1,null,2]
<strong>Output:
</strong> false</code></pre>

**Example 3:**

![](https://assets.leetcode.com/uploads/2020/12/20/ex3.jpg)

<pre><code>Input: p = [1,2,1], q = [1,1,2]
<strong>Output:
</strong> false</code></pre>

&#x20;

**Constraints:**

* The number of nodes in both trees is in the range `[0, 100]`.
* `-104 <= Node.val <= 104`
