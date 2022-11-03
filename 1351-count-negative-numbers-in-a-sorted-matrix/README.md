# 1351. Count Negative Numbers in a Sorted Matrix

## Easy

***

Given a `m x n` matrix `grid` which is sorted in non-increasing order both row-wise and column-wise, return _the number of **negative** numbers in_ `grid`.

&#x20;

**Example 1:**

<pre><code>Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
<strong>Output:
</strong> 8
<strong>Explanation:
</strong> There are 8 negatives number in the matrix.</code></pre>

**Example 2:**

<pre><code>Input: grid = [[3,2],[1,0]]
<strong>Output:
</strong> 0</code></pre>

&#x20;

**Constraints:**

* `m == grid.length`
* `n == grid[i].length`
* `1 <= m, n <= 100`
* `-100 <= grid[i][j] <= 100`

&#x20;

**Follow up:** Could you find an `O(n + m)` solution?
