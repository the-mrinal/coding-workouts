# Evaluate Reverse Polish Notation

***

Evaluate the value of an arithmetic expression in [Reverse Polish Notation](http://en.wikipedia.org/wiki/Reverse\_Polish\_notation).

Valid operators are `+`, `-`, `*`, and `/`. Each operand may be an integer or another expression.

**Note** that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

&#x20;

**Example 1:**

<pre><code>Input: tokens = ["2","1","+","3","*"]
<strong>Output:
</strong> 9
<strong>Explanation:
</strong> ((2 + 1) * 3) = 9</code></pre>

**Example 2:**

<pre><code>Input: tokens = ["4","13","5","/","+"]
<strong>Output:
</strong> 6
<strong>Explanation:
</strong> (4 + (13 / 5)) = 6</code></pre>

**Example 3:**

<pre><code>Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
<strong>Output:
</strong> 22
<strong>Explanation:
</strong> ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22</code></pre>

&#x20;

**Constraints:**

* `1 <= tokens.length <= 104`
* `tokens[i]` is either an operator: `"+"`, `"-"`, `"*"`, or `"/"`, or an integer in the range `[-200, 200]`.
