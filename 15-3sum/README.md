# 15. 3Sum

## Medium

***

Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

&#x20;

**Example 1:**

<pre><code>Input: nums = [-1,0,1,2,-1,-4]
<strong>Output:
</strong> [[-1,-1,2],[-1,0,1]]
<strong>Explanation:
</strong> 
nums[0] + nums[1] + nums[1] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.</code></pre>

**Example 2:**

<pre><code>Input: nums = [0,1,1]
<strong>Output:
</strong> []
<strong>Explanation:
</strong> The only possible triplet does not sum up to 0.</code></pre>

**Example 3:**

<pre><code>Input: nums = [0,0,0]
<strong>Output:
</strong> [[0,0,0]]
<strong>Explanation:
</strong> The only possible triplet sums up to 0.</code></pre>

&#x20;

**Constraints:**

* `3 <= nums.length <= 3000`
* `-105 <= nums[i] <= 105`
