# 55. Jump Game

## Medium

***

You are given an integer array `nums`. You are initially positioned at the array's **first index**, and each element in the array represents your maximum jump length at that position.

Return `true` _if you can reach the last index, or_ `false` _otherwise_.

&#x20;

**Example 1:**

<pre><code>Input: nums = [2,3,1,1,4]
<strong>Output:
</strong> true
<strong>Explanation:
</strong> Jump 1 step from index 0 to 1, then 3 steps to the last index.</code></pre>

**Example 2:**

<pre><code>Input: nums = [3,2,1,0,4]
<strong>Output:
</strong> false
<strong>Explanation:
</strong> You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.</code></pre>

&#x20;

**Constraints:**

* `1 <= nums.length <= 104`
* `0 <= nums[i] <= 105`
