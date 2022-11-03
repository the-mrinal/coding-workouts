# 259. 3Sum Smaller

## Medium

***

Given an array of `n` integers `nums` and an integer `target`, find the number of index triplets `i`, `j`, `k` with `0 <= i < j < k < n` that satisfy the condition `nums[i] + nums[j] + nums[k] < target`.

&#x20;

**Example 1:**

<pre><code>Input: nums = [-2,0,1,3], target = 2
<strong>Output:
</strong> 2
<strong>Explanation:
</strong> Because there are two triplets which sums are less than 2:
[-2,0,1]
[-2,0,3]</code></pre>

**Example 2:**

<pre><code>Input: nums = [], target = 0
<strong>Output:
</strong> 0</code></pre>

**Example 3:**

<pre><code>Input: nums = [0], target = 0
<strong>Output:
</strong> 0</code></pre>

&#x20;

**Constraints:**

* `n == nums.length`
* `0 <= n <= 3500`
* `-100 <= nums[i] <= 100`
* `-100 <= target <= 100`
