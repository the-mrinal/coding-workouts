# Rotting Oranges

***

You are given an `m x n` `grid` where each cell can have one of three values:

* `0` representing an empty cell,
* `1` representing a fresh orange, or
* `2` representing a rotten orange.

Every minute, any fresh orange that is **4-directionally adjacent** to a rotten orange becomes rotten.

Return _the minimum number of minutes that must elapse until no cell has a fresh orange_. If _this is impossible, return_ `-1`.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/02/16/oranges.png)

<pre><code>Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
<strong>Output:
</strong> 4</code></pre>

**Example 2:**

<pre><code>Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
<strong>Output:
</strong> -1
<strong>Explanation:
</strong> The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.</code></pre>

**Example 3:**

<pre><code>Input: grid = [[0,2]]
<strong>Output:
</strong> 0
<strong>Explanation:
</strong> Since there are already no fresh oranges at minute 0, the answer is just 0.</code></pre>

&#x20;

**Constraints:**

* `m == grid.length`
* `n == grid[i].length`
* `1 <= m, n <= 10`
* `grid[i][j]` is `0`, `1`, or `2`.
