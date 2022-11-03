# 678. Valid Parenthesis String

## Medium

***

Given a string `s` containing only three types of characters: `'('`, `')'` and `'*'`, return `true` _if_ `s` _is **valid**_.

The following rules define a **valid** string:

* Any left parenthesis `'('` must have a corresponding right parenthesis `')'`.
* Any right parenthesis `')'` must have a corresponding left parenthesis `'('`.
* Left parenthesis `'('` must go before the corresponding right parenthesis `')'`.
* `'*'` could be treated as a single right parenthesis `')'` or a single left parenthesis `'('` or an empty string `""`.

&#x20;

**Example 1:**

<pre><code>Input: s = "()"
<strong>Output:
</strong> true</code></pre>

**Example 2:**

<pre><code>Input: s = "(*)"
<strong>Output:
</strong> true</code></pre>

**Example 3:**

<pre><code>Input: s = "(*))"
<strong>Output:
</strong> true</code></pre>

&#x20;

**Constraints:**

* `1 <= s.length <= 100`
* `s[i]` is `'('`, `')'` or `'*'`.
