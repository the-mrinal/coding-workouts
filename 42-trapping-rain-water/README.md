# 42. Trapping Rain Water

## Hard

***

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png)

<pre><code>Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
<strong>Output:
</strong> 6
<strong>Explanation:
</strong> The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.</code></pre>

**Example 2:**

<pre><code>Input: height = [4,2,0,3,2,5]
<strong>Output:
</strong> 9</code></pre>

&#x20;

**Constraints:**

* `n == height.length`
* `1 <= n <= 2 * 104`
* `0 <= height[i] <= 105`
