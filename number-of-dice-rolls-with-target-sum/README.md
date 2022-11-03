# Number of Dice Rolls With Target Sum

***

You have `n` dice and each die has `k` faces numbered from `1` to `k`.

Given three integers `n`, `k`, and `target`, return _the number of possible ways (out of the_ `kn` _total ways) to roll the dice so the sum of the face-up numbers equals_ `target`. Since the answer may be too large, return it **modulo** `109 + 7`.

&#x20;

**Example 1:**

<pre><code>Input: n = 1, k = 6, target = 3
<strong>Output:
</strong> 1
<strong>Explanation:
</strong> You throw one die with 6 faces.
There is only one way to get a sum of 3.</code></pre>

**Example 2:**

<pre><code>Input: n = 2, k = 6, target = 7
<strong>Output:
</strong> 6
<strong>Explanation:
</strong> You throw two dice, each with 6 faces.
There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.</code></pre>

**Example 3:**

<pre><code>Input: n = 30, k = 30, target = 500
<strong>Output:
</strong> 222616187
<strong>Explanation:
</strong> The answer must be returned modulo 109 + 7.</code></pre>

&#x20;

**Constraints:**

* `1 <= n, k <= 30`
* `1 <= target <= 1000`
