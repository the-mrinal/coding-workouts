# 456. 132 Pattern

## Medium

***

Given an array of `n` integers `nums`, a **132 pattern** is a subsequence of three integers `nums[i]`, `nums[j]` and `nums[k]` such that `i < j < k` and `nums[i] < nums[k] < nums[j]`.

Return `true` _if there is a **132 pattern** in_ `nums`_, otherwise, return_ `false`_._

&#x20;

**Example 1:**

<pre><code>Input: nums = [1,2,3,4]
<strong>Output:
</strong> false
<strong>Explanation:
</strong> There is no 132 pattern in the sequence.</code></pre>

**Example 2:**

<pre><code>Input: nums = [3,1,4,2]
<strong>Output:
</strong> true
<strong>Explanation:
</strong> There is a 132 pattern in the sequence: [1, 4, 2].</code></pre>

**Example 3:**

<pre><code>Input: nums = [-1,3,2,0]
<strong>Output:
</strong> true
<strong>Explanation:
</strong> There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].</code></pre>

&#x20;

**Constraints:**

* `n == nums.length`
* `1 <= n <= 2 * 105`
* `-109 <= nums[i] <= 109`
