# 1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts

## Medium

***

You are given a rectangular cake of size `h x w` and two arrays of integers `horizontalCuts` and `verticalCuts` where:

* `horizontalCuts[i]` is the distance from the top of the rectangular cake to the `ith` horizontal cut and similarly, and
* `verticalCuts[j]` is the distance from the left of the rectangular cake to the `jth` vertical cut.

Return _the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays_ `horizontalCuts` _and_ `verticalCuts`. Since the answer can be a large number, return this **modulo** `109 + 7`.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/05/14/leetcode\_max\_area\_2.png)

<pre><code>Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
<strong>Output:
</strong> 4 
<strong>Explanation:
</strong> The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green piece of cake has the maximum area.</code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/05/14/leetcode\_max\_area\_3.png)

<pre><code>Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
<strong>Output:
</strong> 6
<strong>Explanation:
</strong> The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green and yellow pieces of cake have the maximum area.</code></pre>

**Example 3:**

<pre><code>Input: h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
<strong>Output:
</strong> 9</code></pre>

&#x20;

**Constraints:**

* `2 <= h, w <= 109`
* `1 <= horizontalCuts.length <= min(h - 1, 105)`
* `1 <= verticalCuts.length <= min(w - 1, 105)`
* `1 <= horizontalCuts[i] < h`
* `1 <= verticalCuts[i] < w`
* All the elements in `horizontalCuts` are distinct.
* All the elements in `verticalCuts` are distinct.
