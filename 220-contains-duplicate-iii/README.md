# 220. Contains Duplicate III

## Medium

***

Given an integer array `nums` and two integers `k` and `t`, return `true` if there are **two distinct indices** `i` and `j` in the array such that `abs(nums[i] - nums[j]) <= t` and `abs(i - j) <= k`.

&#x20;

**Example 1:**

<pre><code>Input: nums = [1,2,3,1], k = 3, t = 0
<strong>Output:
</strong> true</code></pre>

**Example 2:**

<pre><code>Input: nums = [1,0,1,1], k = 1, t = 2
<strong>Output:
</strong> true</code></pre>

**Example 3:**

<pre><code>Input: nums = [1,5,9,1,5,9], k = 2, t = 3
<strong>Output:
</strong> false</code></pre>

&#x20;

**Constraints:**

* `1 <= nums.length <= 2 * 104`
* `-231 <= nums[i] <= 231 - 1`
* `0 <= k <= 104`
* `0 <= t <= 231 - 1`
