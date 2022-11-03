# Minimum Falling Path Sum

***

Given an `n x n` array of integers `matrix`, return _the **minimum sum** of any **falling path** through_ `matrix`.

A **falling path** starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position `(row, col)` will be `(row + 1, col - 1)`, `(row + 1, col)`, or `(row + 1, col + 1)`.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/11/03/failing1-grid.jpg)

<pre><code>Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
<strong>Output:
</strong> 13
<strong>Explanation:
</strong> There are two falling paths with a minimum sum as shown.</code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/11/03/failing2-grid.jpg)

<pre><code>Input: matrix = [[-19,57],[-40,-5]]
<strong>Output:
</strong> -59
<strong>Explanation:
</strong> The falling path with a minimum sum is shown.</code></pre>

&#x20;

**Constraints:**

* `n == matrix.length == matrix[i].length`
* `1 <= n <= 100`
* `-100 <= matrix[i][j] <= 100`
