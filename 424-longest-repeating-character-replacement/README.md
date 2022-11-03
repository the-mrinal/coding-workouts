# 424. Longest Repeating Character Replacement

## Medium

***

You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return _the length of the longest substring containing the same letter you can get after performing the above operations_.

&#x20;

**Example 1:**

<pre><code>Input: s = "ABAB", k = 2
<strong>Output:
</strong> 4
<strong>Explanation:
</strong> Replace the two 'A's with two 'B's or vice versa.</code></pre>

**Example 2:**

<pre><code>Input: s = "AABABBA", k = 1
<strong>Output:
</strong> 4
<strong>Explanation:
</strong> Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.</code></pre>

&#x20;

**Constraints:**

* `1 <= s.length <= 105`
* `s` consists of only uppercase English letters.
* `0 <= k <= s.length`
