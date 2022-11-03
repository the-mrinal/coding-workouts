# Minimum Difficulty of a Job Schedule

***

You want to schedule a list of jobs in `d` days. Jobs are dependent (i.e To work on the `ith` job, you have to finish all the jobs `j` where `0 <= j < i`).

You have to finish **at least** one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the `d` days. The difficulty of a day is the maximum difficulty of a job done on that day.

You are given an integer array `jobDifficulty` and an integer `d`. The difficulty of the `ith` job is `jobDifficulty[i]`.

Return _the minimum difficulty of a job schedule_. If you cannot find a schedule for the jobs return `-1`.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/01/16/untitled.png)

<pre><code>Input: jobDifficulty = [6,5,4,3,2,1], d = 2
<strong>Output:
</strong> 7
<strong>Explanation:
</strong> First day you can finish the first 5 jobs, total difficulty = 6.
Second day you can finish the last job, total difficulty = 1.
The difficulty of the schedule = 6 + 1 = 7 </code></pre>

**Example 2:**

<pre><code>Input: jobDifficulty = [9,9,9], d = 4
<strong>Output:
</strong> -1
<strong>Explanation:
</strong> If you finish a job per day you will still have a free day. you cannot find a schedule for the given jobs.</code></pre>

**Example 3:**

<pre><code>Input: jobDifficulty = [1,1,1], d = 3
<strong>Output:
</strong> 3
<strong>Explanation:
</strong> The schedule is one job per day. total difficulty will be 3.</code></pre>

&#x20;

**Constraints:**

* `1 <= jobDifficulty.length <= 300`
* `0 <= jobDifficulty[i] <= 1000`
* `1 <= d <= 10`
