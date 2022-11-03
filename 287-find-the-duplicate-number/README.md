# 287. Find the Duplicate Number

## Medium

***

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.

There is only **one repeated number** in `nums`, return _this repeated number_.

You must solve the problem **without** modifying the array `nums` and uses only constant extra space.

&#x20;

**Example 1:**

<pre><code>Input: nums = [1,3,4,2,2]
<strong>Output:
</strong> 2</code></pre>

**Example 2:**

<pre><code>Input: nums = [3,1,3,4,2]
<strong>Output:
</strong> 3</code></pre>

&#x20;

**Constraints:**

* `1 <= n <= 105`
* `nums.length == n + 1`
* `1 <= nums[i] <= n`
* All the integers in `nums` appear only **once** except for **precisely one integer** which appears **two or more** times.

&#x20;

**Follow up:**

* How can we prove that at least one duplicate number must exist in `nums`?
* Can you solve the problem in linear runtime complexity?
