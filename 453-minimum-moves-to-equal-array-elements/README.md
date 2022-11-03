# 453. Minimum Moves to Equal Array Elements

## Medium

***

Given an integer array `nums` of size `n`, return _the minimum number of moves required to make all array elements equal_.

In one move, you can increment `n - 1` elements of the array by `1`.

&#x20;

**Example 1:**

<pre><code>Input: nums = [1,2,3]
<strong>Output:
</strong> 3
<strong>Explanation:
</strong> Only three moves are needed (remember each move increments two elements):
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]</code></pre>

**Example 2:**

<pre><code>Input: nums = [1,1,1]
<strong>Output:
</strong> 0</code></pre>

&#x20;

**Constraints:**

* `n == nums.length`
* `1 <= nums.length <= 105`
* `-109 <= nums[i] <= 109`
* The answer is guaranteed to fit in a **32-bit** integer.
