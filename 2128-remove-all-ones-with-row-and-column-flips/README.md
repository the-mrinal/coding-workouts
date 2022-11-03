# 2128. Remove All Ones With Row and Column Flips

## Medium

***

You are given an `m x n` binary matrix `grid`.

In one operation, you can choose **any** row or column and flip each value in that row or column (i.e., changing all `0`'s to `1`'s, and all `1`'s to `0`'s).

Return `true` _if it is possible to remove all_ `1`_'s from_ `grid` using **any** number of operations or `false` otherwise.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2022/01/03/image-20220103191300-1.png)

<pre><code>Input: grid = [[0,1,0],[1,0,1],[0,1,0]]
<strong>Output:
</strong> true
<strong>Explanation:
</strong> One possible way to remove all 1's from grid is to:
- Flip the middle row
- Flip the middle column</code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2022/01/03/image-20220103181204-7.png)

<pre><code>Input: grid = [[1,1,0],[0,0,0],[0,0,0]]
<strong>Output:
</strong> false
<strong>Explanation:
</strong> It is impossible to remove all 1's from grid.</code></pre>

**Example 3:**

![](https://assets.leetcode.com/uploads/2022/01/03/image-20220103181224-8.png)

<pre><code>Input: grid = [[0]]
<strong>Output:
</strong> true
<strong>Explanation:
</strong> There are no 1's in grid.</code></pre>

&#x20;

**Constraints:**

* `m == grid.length`
* `n == grid[i].length`
* `1 <= m, n <= 300`
* `grid[i][j]` is either `0` or `1`.
