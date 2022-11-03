# 704. Binary Search

## Easy

***

Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with `O(log n)` runtime complexity.

&#x20;

**Example 1:**

<pre><code>Input: nums = [-1,0,3,5,9,12], target = 9
<strong>Output:
</strong> 4
<strong>Explanation:
</strong> 9 exists in nums and its index is 4</code></pre>

**Example 2:**

<pre><code>Input: nums = [-1,0,3,5,9,12], target = 2
<strong>Output:
</strong> -1
<strong>Explanation:
</strong> 2 does not exist in nums so return -1</code></pre>

&#x20;

**Constraints:**

* `1 <= nums.length <= 104`
* `-104 < nums[i], target < 104`
* All the integers in `nums` are **unique**.
* `nums` is sorted in ascending order.
