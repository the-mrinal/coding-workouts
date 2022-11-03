# Number of Connected Components in an Undirected Graph

***

You have a graph of `n` nodes. You are given an integer `n` and an array `edges` where `edges[i] = [ai, bi]` indicates that there is an edge between `ai` and `bi` in the graph.

Return _the number of connected components in the graph_.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/14/conn1-graph.jpg)

<pre><code>Input: n = 5, edges = [[0,1],[1,2],[3,4]]
<strong>Output:
</strong> 2</code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/03/14/conn2-graph.jpg)

<pre><code>Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
<strong>Output:
</strong> 1</code></pre>

&#x20;

**Constraints:**

* `1 <= n <= 2000`
* `1 <= edges.length <= 5000`
* `edges[i].length == 2`
* `0 <= ai <= bi < n`
* `ai != bi`
* There are no repeated edges.
