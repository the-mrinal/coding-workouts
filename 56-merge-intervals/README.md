# 56. Merge Intervals

## Medium

***

Given an array of `intervals` where `intervals[i] = [starti, endi]`, merge all overlapping intervals, and return _an array of the non-overlapping intervals that cover all the intervals in the input_.

&#x20;

**Example 1:**

<pre><code>Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
<strong>Output:
</strong> [[1,6],[8,10],[15,18]]
<strong>Explanation:
</strong> Since intervals [1,3] and [2,6] overlap, merge them into [1,6].</code></pre>

**Example 2:**

<pre><code>Input: intervals = [[1,4],[4,5]]
<strong>Output:
</strong> [[1,5]]
<strong>Explanation:
</strong> Intervals [1,4] and [4,5] are considered overlapping.</code></pre>

&#x20;

**Constraints:**

* `1 <= intervals.length <= 104`
* `intervals[i].length == 2`
* `0 <= starti <= endi <= 104`
