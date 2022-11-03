# Flood Fill

***

An image is represented by an `m x n` integer grid `image` where `image[i][j]` represents the pixel value of the image.

You are also given three integers `sr`, `sc`, and `newColor`. You should perform a **flood fill** on the image starting from the pixel `image[sr][sc]`.

To perform a **flood fill**, consider the starting pixel, plus any pixels connected **4-directionally** to the starting pixel of the same color as the starting pixel, plus any pixels connected **4-directionally** to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with `newColor`.

Return _the modified image after performing the flood fill_.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/06/01/flood1-grid.jpg)

<pre><code>Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
<strong>Output:
</strong> [[2,2,2],[2,2,0],[2,0,1]]
<strong>Explanation:
</strong> From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.</code></pre>

**Example 2:**

<pre><code>Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
<strong>Output:
</strong> [[2,2,2],[2,2,2]]</code></pre>

&#x20;

**Constraints:**

* `m == image.length`
* `n == image[i].length`
* `1 <= m, n <= 50`
* `0 <= image[i][j], newColor < 216`
* `0 <= sr < m`
* `0 <= sc < n`
