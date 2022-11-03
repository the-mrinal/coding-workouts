# 875. Koko Eating Bananas

## Medium

***

Koko loves to eat bananas. There are `n` piles of bananas, the `ith` pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return _the minimum integer_ `k` _such that she can eat all the bananas within_ `h` _hours_.

&#x20;

**Example 1:**

<pre><code>Input: piles = [3,6,7,11], h = 8
<strong>Output:
</strong> 4</code></pre>

**Example 2:**

<pre><code>Input: piles = [30,11,23,4,20], h = 5
<strong>Output:
</strong> 30</code></pre>

**Example 3:**

<pre><code>Input: piles = [30,11,23,4,20], h = 6
<strong>Output:
</strong> 23</code></pre>

&#x20;

**Constraints:**

* `1 <= piles.length <= 104`
* `piles.length <= h <= 109`
* `1 <= piles[i] <= 109`
