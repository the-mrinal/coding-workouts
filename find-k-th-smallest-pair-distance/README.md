# Find K-th Smallest Pair Distance

***

The **distance of a pair** of integers `a` and `b` is defined as the absolute difference between `a` and `b`.

Given an integer array `nums` and an integer `k`, return _the_ `kth` _smallest **distance among all the pairs**_ `nums[i]` _and_ `nums[j]` _where_ `0 <= i < j < nums.length`.

&#x20;

**Example 1:**

<pre><code>Input: nums = [1,3,1], k = 1
<strong>Output:
</strong> 0
<strong>Explanation:
</strong> Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.</code></pre>

**Example 2:**

<pre><code>Input: nums = [1,1,1], k = 2
<strong>Output:
</strong> 0</code></pre>

**Example 3:**

<pre><code>Input: nums = [1,6,1], k = 3
<strong>Output:
</strong> 5</code></pre>

&#x20;

**Constraints:**

* `n == nums.length`
* `2 <= n <= 104`
* `0 <= nums[i] <= 106`
* `1 <= k <= n * (n - 1) / 2`
