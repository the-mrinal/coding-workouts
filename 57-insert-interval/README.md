# 57. Insert Interval

## Medium

***

You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [starti, endi]` represent the start and the end of the `ith` interval and `intervals` is sorted in ascending order by `starti`. You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `starti` and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return `intervals` _after the insertion_.

&#x20;

**Example 1:**

<pre><code>Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
<strong>Output:
</strong> [[1,5],[6,9]]</code></pre>

**Example 2:**

<pre><code>Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
<strong>Output:
</strong> [[1,2],[3,10],[12,16]]
<strong>Explanation:
</strong> Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].</code></pre>

&#x20;

**Constraints:**

* `0 <= intervals.length <= 104`
* `intervals[i].length == 2`
* `0 <= starti <= endi <= 105`
* `intervals` is sorted by `starti` in **ascending** order.
* `newInterval.length == 2`
* `0 <= start <= end <= 105`
