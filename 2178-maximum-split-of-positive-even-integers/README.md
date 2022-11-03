# 2178. Maximum Split of Positive Even Integers

## Medium

***

You are given an integer `finalSum`. Split it into a sum of a **maximum** number of **unique** positive even integers.

* For example, given `finalSum = 12`, the following splits are **valid** (unique positive even integers summing up to `finalSum`): `(12)`, `(2 + 10)`, `(2 + 4 + 6)`, and `(4 + 8)`. Among them, `(2 + 4 + 6)` contains the maximum number of integers. Note that `finalSum` cannot be split into `(2 + 2 + 4 + 4)` as all the numbers should be unique.

Return _a list of integers that represent a valid split containing a **maximum** number of integers_. If no valid split exists for `finalSum`, return _an **empty** list_. You may return the integers in **any** order.

&#x20;

**Example 1:**

<pre><code>Input: finalSum = 12
<strong>Output:
</strong> [2,4,6]
<strong>Explanation:
</strong> The following are valid splits: (12), (2 + 10), (2 + 4 + 6), and (4 + 8).
(2 + 4 + 6) has the maximum number of integers, which is 3. Thus, we return [2,4,6].
Note that [2,6,4], [6,2,4], etc. are also accepted.</code></pre>

**Example 2:**

<pre><code>Input: finalSum = 7
<strong>Output:
</strong> []
<strong>Explanation:
</strong> There are no valid splits for the given finalSum.
Thus, we return an empty array.</code></pre>

**Example 3:**

<pre><code>Input: finalSum = 28
<strong>Output:
</strong> [6,8,2,12]
<strong>Explanation:
</strong> The following are valid splits: (2 + 26), (6 + 8 + 2 + 12), and (4 + 24). 
(6 + 8 + 2 + 12) has the maximum number of integers, which is 4. Thus, we return [6,8,2,12].
Note that [10,2,4,12], [6,2,4,16], etc. are also accepted.</code></pre>

&#x20;

**Constraints:**

* `1 <= finalSum <= 1010`
