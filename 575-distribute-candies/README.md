# 575. Distribute Candies

## Easy

***

Alice has `n` candies, where the `ith` candy is of type `candyType[i]`. Alice noticed that she started to gain weight, so she visited a doctor.

The doctor advised Alice to only eat `n / 2` of the candies she has (`n` is always even). Alice likes her candies very much, and she wants to eat the maximum number of different types of candies while still following the doctor's advice.

Given the integer array `candyType` of length `n`, return _the **maximum** number of different types of candies she can eat if she only eats_ `n / 2` _of them_.

&#x20;

**Example 1:**

<pre><code>Input: candyType = [1,1,2,2,3,3]
<strong>Output:
</strong> 3
<strong>Explanation:
</strong> Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types, she can eat one of each type.</code></pre>

**Example 2:**

<pre><code>Input: candyType = [1,1,2,3]
<strong>Output:
</strong> 2
<strong>Explanation:
</strong> Alice can only eat 4 / 2 = 2 candies. Whether she eats types [1,2], [1,3], or [2,3], she still can only eat 2 different types.</code></pre>

**Example 3:**

<pre><code>Input: candyType = [6,6,6,6]
<strong>Output:
</strong> 1
<strong>Explanation:
</strong> Alice can only eat 4 / 2 = 2 candies. Even though she can eat 2 candies, she only has 1 type.</code></pre>

&#x20;

**Constraints:**

* `n == candyType.length`
* `2 <= n <= 104`
* `n` is even.
* `-105 <= candyType[i] <= 105`
