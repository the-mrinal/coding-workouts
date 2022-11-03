# 51. N-Queens

## Hard

***

The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return _all distinct solutions to the **n-queens puzzle**_. You may return the answer in **any order**.

Each solution contains a distinct board configuration of the n-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space, respectively.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/13/queens.jpg)

<pre><code>Input: n = 4
<strong>Output:
</strong> [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
<strong>Explanation:
</strong> There exist two distinct solutions to the 4-queens puzzle as shown above</code></pre>

**Example 2:**

<pre><code>Input: n = 1
<strong>Output:
</strong> [["Q"]]</code></pre>

&#x20;

**Constraints:**

* `1 <= n <= 9`
