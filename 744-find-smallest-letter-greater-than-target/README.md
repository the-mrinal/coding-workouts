# 744. Find Smallest Letter Greater Than Target

## Easy

***

Given a characters array `letters` that is sorted in **non-decreasing** order and a character `target`, return _the smallest character in the array that is larger than_ `target`.

**Note** that the letters wrap around.

* For example, if `target == 'z'` and `letters == ['a', 'b']`, the answer is `'a'`.

&#x20;

**Example 1:**

<pre><code>Input: letters = ["c","f","j"], target = "a"
<strong>Output:
</strong> "c"</code></pre>

**Example 2:**

<pre><code>Input: letters = ["c","f","j"], target = "c"
<strong>Output:
</strong> "f"</code></pre>

**Example 3:**

<pre><code>Input: letters = ["c","f","j"], target = "d"
<strong>Output:
</strong> "f"</code></pre>

&#x20;

**Constraints:**

* `2 <= letters.length <= 104`
* `letters[i]` is a lowercase English letter.
* `letters` is sorted in **non-decreasing** order.
* `letters` contains at least two different characters.
* `target` is a lowercase English letter.
