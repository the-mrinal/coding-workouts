# 238. Product of Array Except Self

## Medium

***

Given an integer array `nums`, return _an array_ `answer` _such that_ `answer[i]` _is equal to the product of all the elements of_ `nums` _except_ `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

&#x20;

**Example 1:**

<pre><code>Input: nums = [1,2,3,4]
<strong>Output:
</strong> [24,12,8,6]</code></pre>

**Example 2:**

<pre><code>Input: nums = [-1,1,0,-3,3]
<strong>Output:
</strong> [0,0,9,0,0]</code></pre>

&#x20;

**Constraints:**

* `2 <= nums.length <= 105`
* `-30 <= nums[i] <= 30`
* The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

&#x20;

**Follow up:** Can you solve the problem in `O(1)` extra space complexity? (The output array **does not** count as extra space for space complexity analysis.)
