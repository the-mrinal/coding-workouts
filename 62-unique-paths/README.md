# 62. Unique Paths

## Medium

***

There is a robot on an `m x n` grid. The robot is initially located at the **top-left corner** (i.e., `grid[0][0]`). The robot tries to move to the **bottom-right corner** (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

Given the two integers `m` and `n`, return _the number of possible unique paths that the robot can take to reach the bottom-right corner_.

The test cases are generated so that the answer will be less than or equal to `2 * 109`.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/10/22/robot\_maze.png)

<pre><code>Input: m = 3, n = 7
<strong>Output:
</strong> 28</code></pre>

**Example 2:**

<pre><code>Input: m = 3, n = 2
<strong>Output:
</strong> 3
<strong>Explanation:
</strong> From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down</code></pre>

&#x20;

**Constraints:**

* `1 <= m, n <= 100`
