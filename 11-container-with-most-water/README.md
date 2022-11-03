# 11. Container With Most Water

## Medium

***

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return _the maximum amount of water a container can store_.

**Notice** that you may not slant the container.

&#x20;

**Example 1:**

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question\_11.jpg)

<pre><code>Input: height = [1,8,6,2,5,4,8,3,7]
<strong>Output:
</strong> 49
<strong>Explanation:
</strong> The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.</code></pre>

**Example 2:**

<pre><code>Input: height = [1,1]
<strong>Output:
</strong> 1</code></pre>

&#x20;

**Constraints:**

* `n == height.length`
* `2 <= n <= 105`
* `0 <= height[i] <= 104`
