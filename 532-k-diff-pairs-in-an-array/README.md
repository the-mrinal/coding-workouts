# 532. K-diff Pairs in an Array

## Medium

***

Given an array of integers `nums` and an integer `k`, return _the number of **unique** k-diff pairs in the array_.

A **k-diff** pair is an integer pair `(nums[i], nums[j])`, where the following are true:

* `0 <= i, j < nums.length`
* `i != j`
* `nums[i] - nums[j] == k`

**Notice** that `|val|` denotes the absolute value of `val`.

&#x20;

**Example 1:**

<pre><code>Input: nums = [3,1,4,1,5], k = 2
<strong>Output:
</strong> 2
<strong>Explanation:
</strong> There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.</code></pre>

**Example 2:**

<pre><code>Input: nums = [1,2,3,4,5], k = 1
<strong>Output:
</strong> 4
<strong>Explanation:
</strong> There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).</code></pre>

**Example 3:**

<pre><code>Input: nums = [1,3,1,5,4], k = 0
<strong>Output:
</strong> 1
<strong>Explanation:
</strong> There is one 0-diff pair in the array, (1, 1).</code></pre>

&#x20;

**Constraints:**

* `1 <= nums.length <= 104`
* `-107 <= nums[i] <= 107`
* `0 <= k <= 107`
