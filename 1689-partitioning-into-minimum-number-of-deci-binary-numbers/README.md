# 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers

## Medium

***

A decimal number is called **deci-binary** if each of its digits is either `0` or `1` without any leading zeros. For example, `101` and `1100` are **deci-binary**, while `112` and `3001` are not.

Given a string `n` that represents a positive decimal integer, return _the **minimum** number of positive **deci-binary** numbers needed so that they sum up to_ `n`_._

&#x20;

**Example 1:**

<pre><code>Input: n = "32"
<strong>Output:
</strong> 3
<strong>Explanation:
</strong> 10 + 11 + 11 = 32</code></pre>

**Example 2:**

<pre><code>Input: n = "82734"
<strong>Output:
</strong> 8</code></pre>

**Example 3:**

<pre><code>Input: n = "27346209830709182346"
<strong>Output:
</strong> 9</code></pre>

&#x20;

**Constraints:**

* `1 <= n.length <= 105`
* `n` consists of only digits.
* `n` does not contain any leading zeros and represents a positive integer.
