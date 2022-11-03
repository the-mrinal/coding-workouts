# 713. Subarray Product Less Than K

## Medium

***

Given an array of integers `nums` and an integer `k`, return _the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than_ `k`.

&#x20;

**Example 1:**

<pre><code>Input: nums = [10,5,2,6], k = 100
<strong>Output:
</strong> 8
<strong>Explanation:
</strong> The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.</code></pre>

**Example 2:**

<pre><code>Input: nums = [1,2,3], k = 0
<strong>Output:
</strong> 0</code></pre>

&#x20;

**Constraints:**

* `1 <= nums.length <= 3 * 104`
* `1 <= nums[i] <= 1000`
* `0 <= k <= 106`
