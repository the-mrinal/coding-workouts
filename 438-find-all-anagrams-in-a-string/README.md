# 438. Find All Anagrams in a String

## Medium

***

Given two strings `s` and `p`, return _an array of all the start indices of_ `p`_'s anagrams in_ `s`. You may return the answer in **any order**.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

&#x20;

**Example 1:**

<pre><code>Input: s = "cbaebabacd", p = "abc"
<strong>Output:
</strong> [0,6]
<strong>Explanation:
</strong>The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".</code></pre>

**Example 2:**

<pre><code>Input: s = "abab", p = "ab"
<strong>Output:
</strong> [0,1,2]
<strong>Explanation:
</strong>The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".</code></pre>

&#x20;

**Constraints:**

* `1 <= s.length, p.length <= 3 * 104`
* `s` and `p` consist of lowercase English letters.
