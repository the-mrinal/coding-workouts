# 442. Find All Duplicates in an Array

## Medium

***

Given an integer array `nums` of length `n` where all the integers of `nums` are in the range `[1, n]` and each integer appears **once** or **twice**, return _an array of all the integers that appears **twice**_.

You must write an algorithm that runs in `O(n)` time and uses only constant extra space.

&#x20;

**Example 1:**

<pre><code>Input: nums = [4,3,2,7,8,2,3,1]
<strong>Output:
</strong> [2,3]</code></pre>

**Example 2:**

<pre><code>Input: nums = [1,1,2]
<strong>Output:
</strong> [1]</code></pre>

**Example 3:**

<pre><code>Input: nums = [1]
<strong>Output:
</strong> []</code></pre>

&#x20;

**Constraints:**

* `n == nums.length`
* `1 <= n <= 105`
* `1 <= nums[i] <= n`
* Each element in `nums` appears **once** or **twice**.
