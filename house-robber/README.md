# House Robber

***

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given an integer array `nums` representing the amount of money of each house, return _the maximum amount of money you can rob tonight **without alerting the police**_.

&#x20;

**Example 1:**

<pre><code>Input: nums = [1,2,3,1]
<strong>Output:
</strong> 4
<strong>Explanation:
</strong> Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.</code></pre>

**Example 2:**

<pre><code>Input: nums = [2,7,9,3,1]
<strong>Output:
</strong> 12
<strong>Explanation:
</strong> Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.</code></pre>

&#x20;

**Constraints:**

* `1 <= nums.length <= 100`
* `0 <= nums[i] <= 400`
