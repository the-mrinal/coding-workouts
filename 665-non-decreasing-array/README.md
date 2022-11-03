# 665. Non-decreasing Array

## Medium

***

Given an array `nums` with `n` integers, your task is to check if it could become non-decreasing by modifying **at most one element**.

We define an array is non-decreasing if `nums[i] <= nums[i + 1]` holds for every `i` (**0-based**) such that (`0 <= i <= n - 2`).

&#x20;

**Example 1:**

<pre><code>Input: nums = [4,2,3]
<strong>Output:
</strong> true
<strong>Explanation:
</strong> You could modify the first 4 to 1 to get a non-decreasing array.</code></pre>

**Example 2:**

<pre><code>Input: nums = [4,2,1]
<strong>Output:
</strong> false
<strong>Explanation:
</strong> You can't get a non-decreasing array by modify at most one element.</code></pre>

&#x20;

**Constraints:**

* `n == nums.length`
* `1 <= n <= 104`
* `-105 <= nums[i] <= 105`
