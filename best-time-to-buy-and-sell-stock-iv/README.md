# Best Time to Buy and Sell Stock IV

***

You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `ith` day, and an integer `k`.

Find the maximum profit you can achieve. You may complete at most `k` transactions.

**Note:** You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

&#x20;

**Example 1:**

<pre><code>Input: k = 2, prices = [2,4,1]
<strong>Output:
</strong> 2
<strong>Explanation:
</strong> Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.</code></pre>

**Example 2:**

<pre><code>Input: k = 2, prices = [3,2,6,5,0,3]
<strong>Output:
</strong> 7
<strong>Explanation:
</strong> Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.</code></pre>

&#x20;

**Constraints:**

* `0 <= k <= 100`
* `0 <= prices.length <= 1000`
* `0 <= prices[i] <= 1000`
