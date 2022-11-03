# Count Vowels Permutation

***

Given an integer `n`, your task is to count how many strings of length `n` can be formed under the following rules:

* Each character is a lower case vowel (`'a'`, `'e'`, `'i'`, `'o'`, `'u'`)
* Each vowel `'a'` may only be followed by an `'e'`.
* Each vowel `'e'` may only be followed by an `'a'` or an `'i'`.
* Each vowel `'i'` **may not** be followed by another `'i'`.
* Each vowel `'o'` may only be followed by an `'i'` or a `'u'`.
* Each vowel `'u'` may only be followed by an `'a'.`

Since the answer may be too large, return it modulo `10^9 + 7.`

&#x20;

**Example 1:**

<pre><code>Input: n = 1
<strong>Output:
</strong> 5
<strong>Explanation:
</strong> All possible strings are: "a", "e", "i" , "o" and "u".</code></pre>

**Example 2:**

<pre><code>Input: n = 2
<strong>Output:
</strong> 10
<strong>Explanation:
</strong> All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".</code></pre>

**Example 3:**&#x20;

<pre><code>Input: n = 5
<strong>Output:
</strong> 68</code></pre>

&#x20;

**Constraints:**

* `1 <= n <= 2 * 10^4`
