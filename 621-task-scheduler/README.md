# 621. Task Scheduler

## Medium

***

Given a characters array `tasks`, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer `n` that represents the cooldown period between two **same tasks** (the same letter in the array), that is that there must be at least `n` units of time between any two same tasks.

Return _the least number of units of times that the CPU will take to finish all the given tasks_.

&#x20;

**Example 1:**

<pre><code>Input: tasks = ["A","A","A","B","B","B"], n = 2
<strong>Output:
</strong> 8
<strong>Explanation:
</strong> 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.</code></pre>

**Example 2:**

<pre><code>Input: tasks = ["A","A","A","B","B","B"], n = 0
<strong>Output:
</strong> 6
<strong>Explanation:
</strong> On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.</code></pre>

**Example 3:**

<pre><code>Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
<strong>Output:
</strong> 16
<strong>Explanation:
</strong> 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A</code></pre>

&#x20;

**Constraints:**

* `1 <= task.length <= 104`
* `tasks[i]` is upper-case English letter.
* The integer `n` is in the range `[0, 100]`.
