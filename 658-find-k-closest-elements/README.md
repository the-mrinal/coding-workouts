# 658. Find K Closest Elements

## Medium

***

Given a **sorted** integer array `arr`, two integers `k` and `x`, return the `k` closest integers to `x` in the array. The result should also be sorted in ascending order.

An integer `a` is closer to `x` than an integer `b` if:

* `|a - x| < |b - x|`, or
* `|a - x| == |b - x|` and `a < b`

&#x20;

**Example 1:**

<pre><code>Input: arr = [1,2,3,4,5], k = 4, x = 3
<strong>Output:
</strong> [1,2,3,4]</code></pre>

**Example 2:**

<pre><code>Input: arr = [1,2,3,4,5], k = 4, x = -1
<strong>Output:
</strong> [1,2,3,4]</code></pre>

&#x20;

**Constraints:**

* `1 <= k <= arr.length`
* `1 <= arr.length <= 104`
* `arr` is sorted in **ascending** order.
* `-104 <= arr[i], x <= 104`
