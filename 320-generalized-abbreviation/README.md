# 320. Generalized Abbreviation

## Medium

***

A word's **generalized abbreviation** can be constructed by taking any number of **non-overlapping** and **non-adjacent** substrings and replacing them with their respective lengths.

*   For example, `"abcde"` can be abbreviated into:

    ```
    <ul>
    	<li><code>"a3e"</code> (<code>"bcd"</code> turned into <code>"3"</code>)</li>
    	<li><code>"1bcd1"</code> (<code>"a"</code> and <code>"e"</code> both turned into <code>"1"</code>)</li>
    	<li><code>"5"</code> (<code>"abcde"</code> turned into <code>"5"</code>)</li>
    	<li><code>"abcde"</code> (no substrings replaced)</li>
    </ul>
    </li>
    <li>However, these abbreviations are <strong>invalid</strong>:
    <ul>
    	<li><code>"23"</code> (<code>"ab"</code> turned into <code>"2"</code> and <code>"cde"</code> turned into <code>"3"</code>) is invalid as the substrings chosen are adjacent.</li>
    	<li><code>"22de"</code> (<code>"ab"</code> turned into <code>"2"</code> and <code>"bc"</code> turned into <code>"2"</code>) is invalid as the substring chosen overlap.</li>
    </ul>
    </li>
    ```

Given a string `word`, return _a list of all the possible **generalized abbreviations** of_ `word`. Return the answer in **any order**.

&#x20;

**Example 1:**

<pre><code>Input: word = "word"
<strong>Output:
</strong> ["4","3d","2r1","2rd","1o2","1o1d","1or1","1ord","w3","w2d","w1r1","w1rd","wo2","wo1d","wor1","word"]</code></pre>

**Example 2:**

<pre><code>Input: word = "a"
<strong>Output:
</strong> ["1","a"]</code></pre>

&#x20;

**Constraints:**

* `1 <= word.length <= 15`
* `word` consists of only lowercase English letters.
