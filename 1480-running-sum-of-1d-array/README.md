# 1480. Running Sum of 1d Array

## Easy

***

Given an array `nums`. We define a running sum of an array as `runningSum[i] = sum(nums[0]…nums[i])`.

Return the running sum of `nums`.

&#x20;

**Example 1:**

<pre><code>Input: nums = [1,2,3,4]
<strong>Output:
</strong> [1,3,6,10]
<strong>Explanation:
</strong> Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].</code></pre>

**Example 2:**

<pre><code>Input: nums = [1,1,1,1,1]
<strong>Output:
</strong> [1,2,3,4,5]
<strong>Explanation:
</strong> Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].</code></pre>

**Example 3:**

<pre><code>Input: nums = [3,1,2,10,1]
<strong>Output:
</strong> [3,4,6,16,17]</code></pre>

&#x20;

**Constraints:**

* `1 <= nums.length <= 1000`
* `-10^6 <= nums[i] <= 10^6`
