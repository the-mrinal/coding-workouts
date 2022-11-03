# 374. Guess Number Higher or Lower

## Easy

***

We are playing the Guess Game. The game is as follows:

I pick a number from `1` to `n`. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API `int guess(int num)`, which returns three possible results:

* `-1`: Your guess is higher than the number I picked (i.e. `num > pick`).
* `1`: Your guess is lower than the number I picked (i.e. `num < pick`).
* `0`: your guess is equal to the number I picked (i.e. `num == pick`).

Return _the number that I picked_.

&#x20;

**Example 1:**

<pre><code>Input: n = 10, pick = 6
<strong>Output:
</strong> 6</code></pre>

**Example 2:**

<pre><code>Input: n = 1, pick = 1
<strong>Output:
</strong> 1</code></pre>

**Example 3:**

<pre><code>Input: n = 2, pick = 1
<strong>Output:
</strong> 1</code></pre>

&#x20;

**Constraints:**

* `1 <= n <= 231 - 1`
* `1 <= pick <= n`
