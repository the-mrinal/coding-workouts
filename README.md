# 01 Matrix

***

Given an `m x n` binary matrix `mat`, return _the distance of the nearest_ `0` _for each cell_.

The distance between two adjacent cells is `1`.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/04/24/01-1-grid.jpg)

<pre><code>Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
<strong>Output:
</strong> [[0,0,0],[0,1,0],[0,0,0]]</code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/04/24/01-2-grid.jpg)

<pre><code>Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
<strong>Output:
</strong> [[0,0,0],[0,1,0],[1,2,1]]</code></pre>

&#x20;

**Constraints:**

* `m == mat.length`
* `n == mat[i].length`
* `1 <= m, n <= 104`
* `1 <= m * n <= 104`
* `mat[i][j]` is either `0` or `1`.
* There is at least one `0` in `mat`.
