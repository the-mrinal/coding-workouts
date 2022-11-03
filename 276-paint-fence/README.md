# 276. Paint Fence

## Medium

***

You are painting a fence of `n` posts with `k` different colors. You must paint the posts following these rules:

* Every post must be painted **exactly one** color.
* There **cannot** be three or more **consecutive** posts with the same color.

Given the two integers `n` and `k`, return _the **number of ways** you can paint the fence_.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/28/paintfenceex1.png)

<pre><code>Input: n = 3, k = 2
<strong>Output:
</strong> 6
<strong>Explanation: 
</strong>All the possibilities are shown.
Note that painting all the posts red or all the posts green is invalid because there cannot be three posts in a row with the same color.</code></pre>

**Example 2:**

<pre><code>Input: n = 1, k = 1
<strong>Output:
</strong> 1</code></pre>

**Example 3:**

<pre><code>Input: n = 7, k = 2
<strong>Output:
</strong> 42</code></pre>

&#x20;

**Constraints:**

* `1 <= n <= 50`
* `1 <= k <= 105`
* The testcases are generated such that the answer is in the range `[0, 231 - 1]` for the given `n` and `k`.
