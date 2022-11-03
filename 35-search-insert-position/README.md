# 35. Search Insert Position

## Easy

***

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

&#x20;

**Example 1:**

<pre><code>Input: nums = [1,3,5,6], target = 5
<strong>Output:
</strong> 2</code></pre>

**Example 2:**

<pre><code>Input: nums = [1,3,5,6], target = 2
<strong>Output:
</strong> 1</code></pre>

**Example 3:**

<pre><code>Input: nums = [1,3,5,6], target = 7
<strong>Output:
</strong> 4</code></pre>

&#x20;

**Constraints:**

* `1 <= nums.length <= 104`
* `-104 <= nums[i] <= 104`
* `nums` contains **distinct** values sorted in **ascending** order.
* `-104 <= target <= 104`
