# 1319. Number of Operations to Make Network Connected

## Medium

***

There are `n` computers numbered from `0` to `n - 1` connected by ethernet cables `connections` forming a network where `connections[i] = [ai, bi]` represents a connection between computers `ai` and `bi`. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network `connections`. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return _the minimum number of times you need to do this in order to make all the computers connected_. If it is not possible, return `-1`.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/01/02/sample\_1\_1677.png)

<pre><code>Input: n = 4, connections = [[0,1],[0,2],[1,2]]
<strong>Output:
</strong> 1
<strong>Explanation:
</strong> Remove cable between computer 1 and 2 and place between computers 1 and 3.</code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/01/02/sample\_2\_1677.png)

<pre><code>Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
<strong>Output:
</strong> 2</code></pre>

**Example 3:**

<pre><code>Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
<strong>Output:
</strong> -1
<strong>Explanation:
</strong> There are not enough cables.</code></pre>

&#x20;

**Constraints:**

* `1 <= n <= 105`
* `1 <= connections.length <= min(n * (n - 1) / 2, 105)`
* `connections[i].length == 2`
* `0 <= ai, bi < n`
* `ai != bi`
* There are no repeated connections.
* No two computers are connected by more than one cable.
