# 1886. Determine Whether Matrix Can Be Obtained By Rotation

## Easy

***

Given two `n x n` binary matrices `mat` and `target`, return `true` _if it is possible to make_ `mat` _equal to_ `target` _by **rotating** _ `mat` _in **90-degree increments**, or_ `false` _otherwise._

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/05/20/grid3.png)

<pre><code>Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
<strong>Output:
</strong> true
<strong>Explanation: 
</strong>We can rotate mat 90 degrees clockwise to make mat equal target.</code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/05/20/grid4.png)

<pre><code>Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
<strong>Output:
</strong> false
<strong>Explanation:
</strong> It is impossible to make mat equal to target by rotating mat.</code></pre>

**Example 3:**

![](https://assets.leetcode.com/uploads/2021/05/26/grid4.png)

<pre><code>Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
<strong>Output:
</strong> true
<strong>Explanation: 
</strong>We can rotate mat 90 degrees clockwise two times to make mat equal target.</code></pre>

&#x20;

**Constraints:**

* `n == mat.length == target.length`
* `n == mat[i].length == target[i].length`
* `1 <= n <= 10`
* `mat[i][j]` and `target[i][j]` are either `0` or `1`.
