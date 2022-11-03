# 1059. All Paths from Source Lead to Destination

## Medium

***

Given the `edges` of a directed graph where `edges[i] = [ai, bi]` indicates there is an edge between nodes `ai` and `bi`, and two nodes `source` and `destination` of this graph, determine whether or not all paths starting from `source` eventually, end at `destination`, that is:

* At least one path exists from the `source` node to the `destination` node
* If a path exists from the `source` node to a node with no outgoing edges, then that node is equal to `destination`.
* The number of possible paths from `source` to `destination` is a finite number.

Return `true` if and only if all roads from `source` lead to `destination`.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/03/16/485\_example\_1.png)

<pre><code>Input: n = 3, edges = [[0,1],[0,2]], source = 0, destination = 2
<strong>Output:
</strong> false
<strong>Explanation:
</strong> It is possible to reach and get stuck on both node 1 and node 2.</code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2019/03/16/485\_example\_2.png)

<pre><code>Input: n = 4, edges = [[0,1],[0,3],[1,2],[2,1]], source = 0, destination = 3
<strong>Output:
</strong> false
<strong>Explanation:
</strong> We have two possibilities: to end at node 3, or to loop over node 1 and node 2 indefinitely.</code></pre>

**Example 3:**

![](https://assets.leetcode.com/uploads/2019/03/16/485\_example\_3.png)

<pre><code>Input: n = 4, edges = [[0,1],[0,2],[1,3],[2,3]], source = 0, destination = 3
<strong>Output:
</strong> true</code></pre>

&#x20;

**Constraints:**

* `1 <= n <= 104`
* `0 <= edges.length <= 104`
* `edges.length == 2`
* `0 <= ai, bi <= n - 1`
* `0 <= source <= n - 1`
* `0 <= destination <= n - 1`
* The given graph may have self-loops and parallel edges.
