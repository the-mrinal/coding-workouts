# 30. Substring with Concatenation of All Words

## Hard

***

You are given a string `s` and an array of strings `words` of **the same length**. Return all starting indices of substring(s) in `s` that is a concatenation of each word in `words` **exactly once**, **in any order**, and **without any intervening characters**.

You can return the answer in **any order**.

&#x20;

**Example 1:**

<pre><code>Input: s = "barfoothefoobarman", words = ["foo","bar"]
<strong>Output:
</strong> [0,9]
<strong>Explanation:
</strong> Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.</code></pre>

**Example 2:**

<pre><code>Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
<strong>Output:
</strong> []</code></pre>

**Example 3:**

<pre><code>Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
<strong>Output:
</strong> [6,9,12]</code></pre>

&#x20;

**Constraints:**

* `1 <= s.length <= 104`
* `s` consists of lower-case English letters.
* `1 <= words.length <= 5000`
* `1 <= words[i].length <= 30`
* `words[i]` consists of lower-case English letters.
