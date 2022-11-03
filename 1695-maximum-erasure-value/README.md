# 1695. Maximum Erasure Value

## Medium

***

You are given an array of positive integers `nums` and want to erase a subarray containing **unique elements**. The **score** you get by erasing the subarray is equal to the **sum** of its elements.

Return _the **maximum score** you can get by erasing **exactly one** subarray._

An array `b` is called to be a subarray of `a` if it forms a contiguous subsequence of `a`, that is, if it is equal to `a[l],a[l+1],...,a[r]` for some `(l,r)`.

&#x20;

**Example 1:**

<pre><code>Input: nums = [4,2,4,5,6]
<strong>Output:
</strong> 17
<strong>Explanation:
</strong> The optimal subarray here is [2,4,5,6].</code></pre>

**Example 2:**

<pre><code>Input: nums = [5,2,1,2,5,2,1,2,5]
<strong>Output:
</strong> 8
<strong>Explanation:
</strong> The optimal subarray here is [5,2,1] or [1,2,5].</code></pre>

&#x20;

**Constraints:**

* `1 <= nums.length <= 105`
* `1 <= nums[i] <= 104`
