# Coin Change

***

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return _the fewest number of coins that you need to make up that amount_. If that amount of money cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an infinite number of each kind of coin.

&#x20;

**Example 1:**

<pre><code>Input: coins = [1,2,5], amount = 11
<strong>Output:
</strong> 3
<strong>Explanation:
</strong> 11 = 5 + 5 + 1</code></pre>

**Example 2:**

<pre><code>Input: coins = [2], amount = 3
<strong>Output:
</strong> -1</code></pre>

**Example 3:**

<pre><code>Input: coins = [1], amount = 0
<strong>Output:
</strong> 0</code></pre>

&#x20;

**Constraints:**

* `1 <= coins.length <= 12`
* `1 <= coins[i] <= 231 - 1`
* `0 <= amount <= 104`
