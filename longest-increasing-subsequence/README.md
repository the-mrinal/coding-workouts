# Longest Increasing Subsequence

***

Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

A **subsequence** is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, `[3,6,2,7]` is a subsequence of the array `[0,3,1,6,2,2,7]`.

&#x20;

**Example 1:**

<pre><code>Input: nums = [10,9,2,5,3,7,101,18]
<strong>Output:
</strong> 4
<strong>Explanation:
</strong> The longest increasing subsequence is [2,3,7,101], therefore the length is 4.</code></pre>

**Example 2:**

<pre><code>Input: nums = [0,1,0,3,2,3]
<strong>Output:
</strong> 4</code></pre>

**Example 3:**

<pre><code>Input: nums = [7,7,7,7,7,7,7]
<strong>Output:
</strong> 1</code></pre>

&#x20;

**Constraints:**

* `1 <= nums.length <= 2500`
* `-104 <= nums[i] <= 104`

&#x20;

**Follow up:** Can you come up with an algorithm that runs in `O(n log(n))` time complexity?
