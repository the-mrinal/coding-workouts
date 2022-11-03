# 1262. Greatest Sum Divisible by Three

## Medium

***

Given an integer array `nums`, return _the **maximum possible sum** of elements of the array such that it is divisible by three_.

&#x20;

**Example 1:**

<pre><code>Input: nums = [3,6,5,1,8]
<strong>Output:
</strong> 18
<strong>Explanation:
</strong> Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).</code></pre>

**Example 2:**

<pre><code>Input: nums = [4]
<strong>Output:
</strong> 0
<strong>Explanation:
</strong> Since 4 is not divisible by 3, do not pick any number.</code></pre>

**Example 3:**

<pre><code>Input: nums = [1,2,3,4,4]
<strong>Output:
</strong> 12
<strong>Explanation:
</strong> Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).</code></pre>

&#x20;

**Constraints:**

* `1 <= nums.length <= 4 * 10^4`
* `1 <= nums[i] <= 10^4`
