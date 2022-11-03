# Maximal Square

***

Given an `m x n` binary `matrix` filled with `0`'s and `1`'s, _find the largest square containing only_ `1`'s _and return its area_.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/26/max1grid.jpg)

<pre><code>Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
<strong>Output:
</strong> 4</code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/11/26/max2grid.jpg)

<pre><code>Input: matrix = [["0","1"],["1","0"]]
<strong>Output:
</strong> 1</code></pre>

**Example 3:**

<pre><code>Input: matrix = [["0"]]
<strong>Output:
</strong> 0</code></pre>

&#x20;

**Constraints:**

* `m == matrix.length`
* `n == matrix[i].length`
* `1 <= m, n <= 300`
* `matrix[i][j]` is `'0'` or `'1'`.
