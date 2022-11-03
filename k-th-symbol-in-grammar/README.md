# K-th Symbol in Grammar

***

We build a table of `n` rows (**1-indexed**). We start by writing `0` in the `1st` row. Now in every subsequent row, we look at the previous row and replace each occurrence of `0` with `01`, and each occurrence of `1` with `10`.

* For example, for `n = 3`, the `1st` row is `0`, the `2nd` row is `01`, and the `3rd` row is `0110`.

Given two integer `n` and `k`, return the `kth` (**1-indexed**) symbol in the `nth` row of a table of `n` rows.

&#x20;

**Example 1:**

<pre><code>Input: n = 1, k = 1
<strong>Output:
</strong> 0
<strong>Explanation:
</strong> row 1: 0</code></pre>

**Example 2:**

<pre><code>Input: n = 2, k = 1
<strong>Output:
</strong> 0
<strong>Explanation:
</strong> 
row 1: 0
row 2: 01</code></pre>

**Example 3:**

<pre><code>Input: n = 2, k = 2
<strong>Output:
</strong> 1
<strong>Explanation:
</strong> 
row 1: 0
row 2: 01</code></pre>

&#x20;

**Constraints:**

* `1 <= n <= 30`
* `1 <= k <= 2n - 1`
