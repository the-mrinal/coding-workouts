# 74. Search a 2D Matrix

## Medium

***

Write an efficient algorithm that searches for a value `target` in an `m x n` integer matrix `matrix`. This matrix has the following properties:

* Integers in each row are sorted from left to right.
* The first integer of each row is greater than the last integer of the previous row.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/05/mat.jpg)

<pre><code>Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
<strong>Output:
</strong> true</code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/10/05/mat2.jpg)

<pre><code>Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
<strong>Output:
</strong> false</code></pre>

&#x20;

**Constraints:**

* `m == matrix.length`
* `n == matrix[i].length`
* `1 <= m, n <= 100`
* `-104 <= matrix[i][j], target <= 104`
