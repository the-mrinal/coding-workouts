# 918. Maximum Sum Circular Subarray

## Medium

***

Given a **circular integer array** `nums` of length `n`, return _the maximum possible sum of a non-empty **subarray** of_ `nums`.

A **circular array** means the end of the array connects to the beginning of the array. Formally, the next element of `nums[i]` is `nums[(i + 1) % n]` and the previous element of `nums[i]` is `nums[(i - 1 + n) % n]`.

A **subarray** may only include each element of the fixed buffer `nums` at most once. Formally, for a subarray `nums[i], nums[i + 1], ..., nums[j]`, there does not exist `i <= k1`, `k2 <= j` with `k1 % n == k2 % n`.

&#x20;

**Example 1:**

<pre><code>Input: nums = [1,-2,3,-2]
<strong>Output:
</strong> 3
<strong>Explanation:
</strong> Subarray [3] has maximum sum 3.</code></pre>

**Example 2:**

<pre><code>Input: nums = [5,-3,5]
<strong>Output:
</strong> 10
<strong>Explanation:
</strong> Subarray [5,5] has maximum sum 5 + 5 = 10.</code></pre>

**Example 3:**

<pre><code>Input: nums = [-3,-2,-3]
<strong>Output:
</strong> -2
<strong>Explanation:
</strong> Subarray [-2] has maximum sum -2.</code></pre>

&#x20;

**Constraints:**

* `n == nums.length`
* `1 <= n <= 3 * 104`
* `-3 * 104 <= nums[i] <= 3 * 104`
