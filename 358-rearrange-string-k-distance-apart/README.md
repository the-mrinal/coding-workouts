# 358. Rearrange String k Distance Apart

## Hard

***

Given a string `s` and an integer `k`, rearrange `s` such that the same characters are **at least** distance `k` from each other. If it is not possible to rearrange the string, return an empty string `""`.

&#x20;

**Example 1:**

<pre><code>Input: s = "aabbcc", k = 3
<strong>Output:
</strong> "abcabc"
<strong>Explanation:
</strong> The same letters are at least a distance of 3 from each other.</code></pre>

**Example 2:**

<pre><code>Input: s = "aaabc", k = 3
<strong>Output:
</strong> ""
<strong>Explanation:
</strong> It is not possible to rearrange the string.</code></pre>

**Example 3:**

<pre><code>Input: s = "aaadbbcc", k = 2
<strong>Output:
</strong> "abacabcd"
<strong>Explanation:
</strong> The same letters are at least a distance of 2 from each other.</code></pre>

&#x20;

**Constraints:**

* `1 <= s.length <= 3 * 105`
* `s` consists of only lowercase English letters.
* `0 <= k <= s.length`
