# 462. Minimum Moves to Equal Array Elements II

## Medium

***

Given an integer array `nums` of size `n`, return _the minimum number of moves required to make all array elements equal_.

In one move, you can increment or decrement an element of the array by `1`.

Test cases are designed so that the answer will fit in a **32-bit** integer.

&#x20;

**Example 1:**

<pre><code>Input: nums = [1,2,3]
<strong>Output:
</strong> 2
<strong>Explanation:
</strong>Only two moves are needed (remember each move increments or decrements one element):
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]</code></pre>

**Example 2:**

<pre><code>Input: nums = [1,10,2,9]
<strong>Output:
</strong> 16</code></pre>

&#x20;

**Constraints:**

* `n == nums.length`
* `1 <= nums.length <= 105`
* `-109 <= nums[i] <= 109`
