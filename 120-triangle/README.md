# 120. Triangle

## Medium

***

Given a `triangle` array, return _the minimum path sum from top to bottom_.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index `i` on the current row, you may move to either index `i` or index `i + 1` on the next row.

&#x20;

**Example 1:**

<pre><code>Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
<strong>Output:
</strong> 11
<strong>Explanation:
</strong> The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).</code></pre>

**Example 2:**

<pre><code>Input: triangle = [[-10]]
<strong>Output:
</strong> -10</code></pre>

&#x20;

**Constraints:**

* `1 <= triangle.length <= 200`
* `triangle[0].length == 1`
* `triangle[i].length == triangle[i - 1].length + 1`
* `-104 <= triangle[i][j] <= 104`

&#x20;

**Follow up:** Could you do this using only `O(n)` extra space, where `n` is the total number of rows in the triangle?
