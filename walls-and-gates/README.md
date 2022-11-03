# Walls and Gates

***

You are given an `m x n` grid `rooms` initialized with these three possible values.

* `-1` A wall or an obstacle.
* `0` A gate.
* `INF` Infinity means an empty room. We use the value `231 - 1 = 2147483647` to represent `INF` as you may assume that the distance to a gate is less than `2147483647`.

Fill each empty room with the distance to _its nearest gate_. If it is impossible to reach a gate, it should be filled with `INF`.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/03/grid.jpg)

<pre><code>Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
<strong>Output:
</strong> [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]</code></pre>

**Example 2:**

<pre><code>Input: rooms = [[-1]]
<strong>Output:
</strong> [[-1]]</code></pre>

&#x20;

**Constraints:**

* `m == rooms.length`
* `n == rooms[i].length`
* `1 <= m, n <= 250`
* `rooms[i][j]` is `-1`, `0`, or `231 - 1`.
