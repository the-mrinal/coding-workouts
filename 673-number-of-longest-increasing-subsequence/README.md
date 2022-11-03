# 673. Number of Longest Increasing Subsequence

## Medium

***

Given an integer array `nums`, return _the number of longest increasing subsequences._

**Notice** that the sequence has to be **strictly** increasing.

&#x20;

**Example 1:**

<pre><code>Input: nums = [1,3,5,4,7]
<strong>Output:
</strong> 2
<strong>Explanation:
</strong> The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].</code></pre>

**Example 2:**

<pre><code>Input: nums = [2,2,2,2,2]
<strong>Output:
</strong> 5
<strong>Explanation:
</strong> The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1, so output 5.</code></pre>

&#x20;

**Constraints:**

* `1 <= nums.length <= 2000`
* `-106 <= nums[i] <= 106`
