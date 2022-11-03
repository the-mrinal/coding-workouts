# 64. Minimum Path Sum

## Medium

***

Given a `m x n` `grid` filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

**Note:** You can only move either down or right at any point in time.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/05/minpath.jpg)

<pre><code>Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
<strong>Output:
</strong> 7
<strong>Explanation:
</strong> Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.</code></pre>

**Example 2:**

<pre><code>Input: grid = [[1,2,3],[4,5,6]]
<strong>Output:
</strong> 12</code></pre>

&#x20;

**Constraints:**

* `m == grid.length`
* `n == grid[i].length`
* `1 <= m, n <= 200`
* `0 <= grid[i][j] <= 100`
