# 209. Minimum Size Subarray Sum

## Medium

***

Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a **contiguous subarray** `[numsl, numsl+1, ..., numsr-1, numsr]` of which the sum is greater than or equal to `target`. If there is no such subarray, return `0` instead.

&#x20;

**Example 1:**

<pre><code>Input: target = 7, nums = [2,3,1,2,4,3]
<strong>Output:
</strong> 2
<strong>Explanation:
</strong> The subarray [4,3] has the minimal length under the problem constraint.</code></pre>

**Example 2:**

<pre><code>Input: target = 4, nums = [1,4,4]
<strong>Output:
</strong> 1</code></pre>

**Example 3:**

<pre><code>Input: target = 11, nums = [1,1,1,1,1,1,1,1]
<strong>Output:
</strong> 0</code></pre>

&#x20;

**Constraints:**

* `1 <= target <= 109`
* `1 <= nums.length <= 105`
* `1 <= nums[i] <= 104`

&#x20;

**Follow up:** If you have figured out the `O(n)` solution, try coding another solution of which the time complexity is `O(n log(n))`.
