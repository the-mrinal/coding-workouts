# 1283. Find the Smallest Divisor Given a Threshold

## Medium

***

Given an array of integers `nums` and an integer `threshold`, we will choose a positive integer `divisor`, divide all the array by it, and sum the division's result. Find the **smallest** `divisor` such that the result mentioned above is less than or equal to `threshold`.

Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example: `7/3 = 3` and `10/2 = 5`).

The test cases are generated so that there will be an answer.

&#x20;

**Example 1:**

<pre><code>Input: nums = [1,2,5,9], threshold = 6
<strong>Output:
</strong> 5
<strong>Explanation:
</strong> We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
If the divisor is 4 we can get a sum of 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2). </code></pre>

**Example 2:**

<pre><code>Input: nums = [44,22,33,11,1], threshold = 5
<strong>Output:
</strong> 44</code></pre>

&#x20;

**Constraints:**

* `1 <= nums.length <= 5 * 104`
* `1 <= nums[i] <= 106`
* `nums.length <= threshold <= 106`
