# Min Cost to Connect All Points

***

You are given an array `points` representing integer coordinates of some points on a 2D-plane, where `points[i] = [xi, yi]`.

The cost of connecting two points `[xi, yi]` and `[xj, yj]` is the **manhattan distance** between them: `|xi - xj| + |yi - yj|`, where `|val|` denotes the absolute value of `val`.

Return _the minimum cost to make all points connected._ All points are connected if there is **exactly one** simple path between any two points.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/08/26/d.png)

<pre><code>Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
<strong>Output:
</strong> 20
<strong>Explanation:
</strong> 

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.</code></pre>

**Example 2:**

<pre><code>Input: points = [[3,12],[-2,5],[-4,1]]
<strong>Output:
</strong> 18</code></pre>

&#x20;

**Constraints:**

* `1 <= points.length <= 1000`
* `-106 <= xi, yi <= 106`
* All pairs `(xi, yi)` are distinct.
