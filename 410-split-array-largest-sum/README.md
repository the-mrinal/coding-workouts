# 410. Split Array Largest Sum

## Hard

***

Given an array `nums` which consists of non-negative integers and an integer `m`, you can split the array into `m` non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these `m` subarrays.

&#x20;

**Example 1:**

<pre><code>Input: nums = [7,2,5,10,8], m = 2
<strong>Output:
</strong> 18
<strong>Explanation:
</strong>There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.</code></pre>

**Example 2:**

<pre><code>Input: nums = [1,2,3,4,5], m = 2
<strong>Output:
</strong> 9</code></pre>

**Example 3:**

<pre><code>Input: nums = [1,4,4], m = 3
<strong>Output:
</strong> 4</code></pre>

&#x20;

**Constraints:**

* `1 <= nums.length <= 1000`
* `0 <= nums[i] <= 106`
* `1 <= m <= min(50, nums.length)`
