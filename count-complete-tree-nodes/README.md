# Count Complete Tree Nodes

***

Given the `root` of a **complete** binary tree, return the number of the nodes in the tree.

According to [**Wikipedia**](http://en.wikipedia.org/wiki/Binary\_tree#Types\_of\_binary\_trees), every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between `1` and `2h` nodes inclusive at the last level `h`.

Design an algorithm that runs in less than `O(n)` time complexity.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/14/complete.jpg)

<pre><code>Input: root = [1,2,3,4,5,6]
<strong>Output:
</strong> 6</code></pre>

**Example 2:**

<pre><code>Input: root = []
<strong>Output:
</strong> 0</code></pre>

**Example 3:**

<pre><code>Input: root = [1]
<strong>Output:
</strong> 1</code></pre>

&#x20;

**Constraints:**

* The number of nodes in the tree is in the range `[0, 5 * 104]`.
* `0 <= Node.val <= 5 * 104`
* The tree is guaranteed to be **complete**.
