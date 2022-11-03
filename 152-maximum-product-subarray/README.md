# 152. Maximum Product Subarray

## Medium

***

Given an integer array `nums`, find a contiguous non-empty subarray within the array that has the largest product, and return _the product_.

The test cases are generated so that the answer will fit in a **32-bit** integer.

A **subarray** is a contiguous subsequence of the array.

&#x20;

**Example 1:**

<pre><code>Input: nums = [2,3,-2,4]
<strong>Output:
</strong> 6
<strong>Explanation:
</strong> [2,3] has the largest product 6.</code></pre>

**Example 2:**

<pre><code>Input: nums = [-2,0,-1]
<strong>Output:
</strong> 0
<strong>Explanation:
</strong> The result cannot be 2, because [-2,-1] is not a subarray.</code></pre>

&#x20;

**Constraints:**

* `1 <= nums.length <= 2 * 104`
* `-10 <= nums[i] <= 10`
* The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.
