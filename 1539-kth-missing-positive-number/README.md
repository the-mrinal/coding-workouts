# 1539. Kth Missing Positive Number

## Easy

***

Given an array `arr` of positive integers sorted in a **strictly increasing order**, and an integer `k`.

Return _the_ `kth` _**positive** integer that is **missing** from this array._

&#x20;

**Example 1:**

<pre><code>Input: arr = [2,3,4,7,11], k = 5
<strong>Output:
</strong> 9
<strong>Explanation: 
</strong>The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.</code></pre>

**Example 2:**

<pre><code>Input: arr = [1,2,3,4], k = 2
<strong>Output:
</strong> 6
<strong>Explanation: 
</strong>The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.</code></pre>

&#x20;

**Constraints:**

* `1 <= arr.length <= 1000`
* `1 <= arr[i] <= 1000`
* `1 <= k <= 1000`
* `arr[i] < arr[j]` for `1 <= i < j <= arr.length`

&#x20;

**Follow up:**

Could you solve this problem in less than O(n) complexity?
