# 867. Transpose Matrix

## Easy

***

Given a 2D integer array `matrix`, return _the **transpose** of_ `matrix`.

The **transpose** of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

![](https://assets.leetcode.com/uploads/2021/02/10/hint\_transpose.png)

&#x20;

**Example 1:**

<pre><code>Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
<strong>Output:
</strong> [[1,4,7],[2,5,8],[3,6,9]]</code></pre>

**Example 2:**

<pre><code>Input: matrix = [[1,2,3],[4,5,6]]
<strong>Output:
</strong> [[1,4],[2,5],[3,6]]</code></pre>

&#x20;

**Constraints:**

* `m == matrix.length`
* `n == matrix[i].length`
* `1 <= m, n <= 1000`
* `1 <= m * n <= 105`
* `-109 <= matrix[i][j] <= 109`
