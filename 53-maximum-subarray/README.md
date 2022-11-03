# 53. Maximum Subarray

## Medium

***

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return _its sum_.

A **subarray** is a **contiguous** part of an array.

&#x20;

**Example 1:**

<pre><code>Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
<strong>Output:
</strong> 6
<strong>Explanation:
</strong> [4,-1,2,1] has the largest sum = 6.</code></pre>

**Example 2:**

<pre><code>Input: nums = [1]
<strong>Output:
</strong> 1</code></pre>

**Example 3:**

<pre><code>Input: nums = [5,4,-1,7,8]
<strong>Output:
</strong> 23</code></pre>

&#x20;

**Constraints:**

* `1 <= nums.length <= 105`
* `-104 <= nums[i] <= 104`

&#x20;

**Follow up:** If you have figured out the `O(n)` solution, try coding another solution using the **divide and conquer** approach, which is more subtle.
