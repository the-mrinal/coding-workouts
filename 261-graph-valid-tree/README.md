# 261. Graph Valid Tree

## Medium

***

You have a graph of `n` nodes labeled from `0` to `n - 1`. You are given an integer n and a list of `edges` where `edges[i] = [ai, bi]` indicates that there is an undirected edge between nodes `ai` and `bi` in the graph.

Return `true` _if the edges of the given graph make up a valid tree, and_ `false` _otherwise_.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/12/tree1-graph.jpg)

<pre><code>Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
<strong>Output:
</strong> true</code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/03/12/tree2-graph.jpg)

<pre><code>Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
<strong>Output:
</strong> false</code></pre>

&#x20;

**Constraints:**

* `1 <= n <= 2000`
* `0 <= edges.length <= 5000`
* `edges[i].length == 2`
* `0 <= ai, bi < n`
* `ai != bi`
* There are no self-loops or repeated edges.
