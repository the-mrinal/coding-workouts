# 1014. Best Sightseeing Pair

## Medium

***

You are given an integer array `values` where values\[i] represents the value of the `ith` sightseeing spot. Two sightseeing spots `i` and `j` have a **distance** `j - i` between them.

The score of a pair (`i < j`) of sightseeing spots is `values[i] + values[j] + i - j`: the sum of the values of the sightseeing spots, minus the distance between them.

Return _the maximum score of a pair of sightseeing spots_.

&#x20;

**Example 1:**

<pre><code>Input: values = [8,1,5,2,6]
<strong>Output:
</strong> 11
<strong>Explanation:
</strong> i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11</code></pre>

**Example 2:**

<pre><code>Input: values = [1,2]
<strong>Output:
</strong> 2</code></pre>

&#x20;

**Constraints:**

* `2 <= values.length <= 5 * 104`
* `1 <= values[i] <= 1000`
