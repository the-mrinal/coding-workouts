# 1202. Smallest String With Swaps

## Medium

***

You are given a string `s`, and an array of pairs of indices in the string `pairs` where `pairs[i] = [a, b]` indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given `pairs` **any number of times**.

Return the lexicographically smallest string that `s` can be changed to after using the swaps.

&#x20;

**Example 1:**

<pre><code>Input: s = "dcab", pairs = [[0,3],[1,2]]
<strong>Output:
</strong> "bacd"
<strong>Explaination:
</strong> 
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"</code></pre>

**Example 2:**

<pre><code>Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
<strong>Output:
</strong> "abcd"
<strong>Explaination: 
</strong>Swap s[0] and s[3], s = "bcad"
Swap s[0] and s[2], s = "acbd"
Swap s[1] and s[2], s = "abcd"</code></pre>

**Example 3:**

<pre><code>Input: s = "cba", pairs = [[0,1],[1,2]]
<strong>Output:
</strong> "abc"
<strong>Explaination: 
</strong>Swap s[0] and s[1], s = "bca"
Swap s[1] and s[2], s = "bac"
Swap s[0] and s[1], s = "abc"</code></pre>

&#x20;

**Constraints:**

* `1 <= s.length <= 10^5`
* `0 <= pairs.length <= 10^5`
* `0 <= pairs[i][0], pairs[i][1] < s.length`
* `s` only contains lower case English letters.
