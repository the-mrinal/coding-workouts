# 219. Contains Duplicate II

## Easy

***

Given an integer array `nums` and an integer `k`, return `true` if there are two **distinct indices** `i` and `j` in the array such that `nums[i] == nums[j]` and `abs(i - j) <= k`.

&#x20;

**Example 1:**

<pre><code>Input: nums = [1,2,3,1], k = 3
<strong>Output:
</strong> true</code></pre>

**Example 2:**

<pre><code>Input: nums = [1,0,1,1], k = 1
<strong>Output:
</strong> true</code></pre>

**Example 3:**

<pre><code>Input: nums = [1,2,3,1,2,3], k = 2
<strong>Output:
</strong> false</code></pre>

&#x20;

**Constraints:**

* `1 <= nums.length <= 105`
* `-109 <= nums[i] <= 109`
* `0 <= k <= 105`
