# Letter Combinations of a Phone Number

***

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in **any order**.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png)

&#x20;

**Example 1:**

<pre><code>Input: digits = "23"
<strong>Output:
</strong> ["ad","ae","af","bd","be","bf","cd","ce","cf"]</code></pre>

**Example 2:**

<pre><code>Input: digits = ""
<strong>Output:
</strong> []</code></pre>

**Example 3:**

<pre><code>Input: digits = "2"
<strong>Output:
</strong> ["a","b","c"]</code></pre>

&#x20;

**Constraints:**

* `0 <= digits.length <= 4`
* `digits[i]` is a digit in the range `['2', '9']`.
