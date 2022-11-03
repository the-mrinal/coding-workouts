# 1048. Longest String Chain

## Medium

***

You are given an array of `words` where each word consists of lowercase English letters.

`wordA` is a **predecessor** of `wordB` if and only if we can insert **exactly one** letter anywhere in `wordA` **without changing the order of the other characters** to make it equal to `wordB`.

* For example, `"abc"` is a **predecessor** of `"abac"`, while `"cba"` is not a **predecessor** of `"bcad"`.

A **word chain** __ is a sequence of words `[word1, word2, ..., wordk]` with `k >= 1`, where `word1` is a **predecessor** of `word2`, `word2` is a **predecessor** of `word3`, and so on. A single word is trivially a **word chain** with `k == 1`.

Return _the **length** of the **longest possible word chain** with words chosen from the given list of_ `words`.

&#x20;

**Example 1:**

<pre><code>Input: words = ["a","b","ba","bca","bda","bdca"]
<strong>Output:
</strong> 4
<strong>Explanation
</strong>: One of the longest word chains is ["a","ba","bda","bdca"].</code></pre>

**Example 2:**

<pre><code>Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
<strong>Output:
</strong> 5
<strong>Explanation:
</strong> All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].</code></pre>

**Example 3:**

<pre><code>Input: words = ["abcd","dbqca"]
<strong>Output:
</strong> 1
<strong>Explanation:
</strong> The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.</code></pre>

&#x20;

**Constraints:**

* `1 <= words.length <= 1000`
* `1 <= words[i].length <= 16`
* `words[i]` only consists of lowercase English letters.
