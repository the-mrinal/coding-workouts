# 45. Jump Game II

## Medium

***

Given an array of non-negative integers `nums`, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

&#x20;

**Example 1:**

<pre><code>Input: nums = [2,3,1,1,4]
<strong>Output:
</strong> 2
<strong>Explanation:
</strong> The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.</code></pre>

**Example 2:**

<pre><code>Input: nums = [2,3,0,1,4]
<strong>Output:
</strong> 2</code></pre>

&#x20;

**Constraints:**

* `1 <= nums.length <= 104`
* `0 <= nums[i] <= 1000`
