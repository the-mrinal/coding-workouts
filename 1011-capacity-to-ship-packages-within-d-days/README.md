# 1011. Capacity To Ship Packages Within D Days

## Medium

***

A conveyor belt has packages that must be shipped from one port to another within `days` days.

The `ith` package on the conveyor belt has a weight of `weights[i]`. Each day, we load the ship with packages on the conveyor belt (in the order given by `weights`). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within `days` days.

&#x20;

**Example 1:**

<pre><code>Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
<strong>Output:
</strong> 15
<strong>Explanation:
</strong> A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.</code></pre>

**Example 2:**

<pre><code>Input: weights = [3,2,2,4,1,4], days = 3
<strong>Output:
</strong> 6
<strong>Explanation:
</strong> A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4</code></pre>

**Example 3:**

<pre><code>Input: weights = [1,2,3,1,1], days = 4
<strong>Output:
</strong> 3
<strong>Explanation:
</strong>1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1</code></pre>

&#x20;

**Constraints:**

* `1 <= days <= weights.length <= 5 * 104`
* `1 <= weights[i] <= 500`
