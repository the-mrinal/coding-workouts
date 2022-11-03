# 139. Word Break

## Medium

***

Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

**Note** that the same word in the dictionary may be reused multiple times in the segmentation.

&#x20;

**Example 1:**

<pre><code>Input: s = "leetcode", wordDict = ["leet","code"]
<strong>Output:
</strong> true
<strong>Explanation:
</strong> Return true because "leetcode" can be segmented as "leet code".</code></pre>

**Example 2:**

<pre><code>Input: s = "applepenapple", wordDict = ["apple","pen"]
<strong>Output:
</strong> true
<strong>Explanation:
</strong> Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.</code></pre>

**Example 3:**

<pre><code>Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
<strong>Output:
</strong> false</code></pre>

&#x20;

**Constraints:**

* `1 <= s.length <= 300`
* `1 <= wordDict.length <= 1000`
* `1 <= wordDict[i].length <= 20`
* `s` and `wordDict[i]` consist of only lowercase English letters.
* All the strings of `wordDict` are **unique**.
