# 34. Find First and Last Position of Element in Sorted Array

## Medium

***

Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with `O(log n)` runtime complexity.

&#x20;

**Example 1:**

<pre><code>Input: nums = [5,7,7,8,8,10], target = 8
<strong>Output:
</strong> [3,4]</code></pre>

**Example 2:**

<pre><code>Input: nums = [5,7,7,8,8,10], target = 6
<strong>Output:
</strong> [-1,-1]</code></pre>

**Example 3:**

<pre><code>Input: nums = [], target = 0
<strong>Output:
</strong> [-1,-1]</code></pre>

&#x20;

**Constraints:**

* `0 <= nums.length <= 105`
* `-109 <= nums[i] <= 109`
* `nums` is a non-decreasing array.
* `-109 <= target <= 109`
