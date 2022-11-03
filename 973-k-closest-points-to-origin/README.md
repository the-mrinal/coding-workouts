# 973. K Closest Points to Origin

## Medium

***

Given an array of `points` where `points[i] = [xi, yi]` represents a point on the **X-Y** plane and an integer `k`, return the `k` closest points to the origin `(0, 0)`.

The distance between two points on the **X-Y** plane is the Euclidean distance (i.e., `√(x1 - x2)2 + (y1 - y2)2`).

You may return the answer in **any order**. The answer is **guaranteed** to be **unique** (except for the order that it is in).

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/03/closestplane1.jpg)

<pre><code>Input: points = [[1,3],[-2,2]], k = 1
<strong>Output:
</strong> [[-2,2]]
<strong>Explanation:
</strong>The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) &#x3C; sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].</code></pre>

**Example 2:**

<pre><code>Input: points = [[3,3],[5,-1],[-2,4]], k = 2
<strong>Output:
</strong> [[3,3],[-2,4]]
<strong>Explanation:
</strong> The answer [[-2,4],[3,3]] would also be accepted.</code></pre>

&#x20;

**Constraints:**

* `1 <= k <= points.length <= 104`
* `-104 < xi, yi < 104`
