# 162. Find Peak Element

## Medium

***

A peak element is an element that is strictly greater than its neighbors.

Given a **0-indexed** integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to **any of the peaks**.

You may imagine that `nums[-1] = nums[n] = -∞`. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in `O(log n)` time.

&#x20;

**Example 1:**

<pre><code>Input: nums = [1,2,3,1]
<strong>Output:
</strong> 2
<strong>Explanation:
</strong> 3 is a peak element and your function should return the index number 2.</code></pre>

**Example 2:**

<pre><code>Input: nums = [1,2,1,3,5,6,4]
<strong>Output:
</strong> 5
<strong>Explanation:
</strong> Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.</code></pre>

&#x20;

**Constraints:**

* `1 <= nums.length <= 1000`
* `-231 <= nums[i] <= 231 - 1`
* `nums[i] != nums[i + 1]` for all valid `i`.
