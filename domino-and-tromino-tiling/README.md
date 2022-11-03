# Domino and Tromino Tiling

***

You have two types of tiles: a `2 x 1` domino shape and a tromino shape. You may rotate these shapes.

![](https://assets.leetcode.com/uploads/2021/07/15/lc-domino.jpg)

Given an integer n, return _the number of ways to tile an_ `2 x n` _board_. Since the answer may be very large, return it **modulo** `109 + 7`.

In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/07/15/lc-domino1.jpg)

<pre><code>Input: n = 3
<strong>Output:
</strong> 5
<strong>Explanation:
</strong> The five different ways are show above.</code></pre>

**Example 2:**

<pre><code>Input: n = 1
<strong>Output:
</strong> 1</code></pre>

&#x20;

**Constraints:**

* `1 <= n <= 1000`
