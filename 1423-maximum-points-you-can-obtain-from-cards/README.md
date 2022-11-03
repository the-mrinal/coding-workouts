# 1423. Maximum Points You Can Obtain from Cards

## Medium

***

There are several cards **arranged in a row**, and each card has an associated number of points. The points are given in the integer array `cardPoints`.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly `k` cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array `cardPoints` and the integer `k`, return the _maximum score_ you can obtain.

&#x20;

**Example 1:**

<pre><code>Input: cardPoints = [1,2,3,4,5,6,1], k = 3
<strong>Output:
</strong> 12
<strong>Explanation:
</strong> After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.</code></pre>

**Example 2:**

<pre><code>Input: cardPoints = [2,2,2], k = 2
<strong>Output:
</strong> 4
<strong>Explanation:
</strong> Regardless of which two cards you take, your score will always be 4.</code></pre>

**Example 3:**

<pre><code>Input: cardPoints = [9,7,7,9,7,7,9], k = 7
<strong>Output:
</strong> 55
<strong>Explanation:
</strong> You have to take all the cards. Your score is the sum of points of all cards.</code></pre>

&#x20;

**Constraints:**

* `1 <= cardPoints.length <= 105`
* `1 <= cardPoints[i] <= 104`
* `1 <= k <= cardPoints.length`
