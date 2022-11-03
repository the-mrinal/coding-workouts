# 1346. Check If N and Its Double Exist

## Easy

***

Given an array `arr` of integers, check if there exists two integers `N` and `M` such that `N` is the double of `M` ( i.e. `N = 2 * M`).

More formally check if there exists two indices `i` and `j` such that :

* `i != j`
* `0 <= i, j < arr.length`
* `arr[i] == 2 * arr[j]`

&#x20;

**Example 1:**

<pre><code>Input: arr = [10,2,5,3]
<strong>Output:
</strong> true
<strong>Explanation:
</strong> N = 10 is the double of M = 5,that is, 10 = 2 * 5.</code></pre>

**Example 2:**

<pre><code>Input: arr = [7,1,14,11]
<strong>Output:
</strong> true
<strong>Explanation:
</strong> N = 14 is the double of M = 7,that is, 14 = 2 * 7.</code></pre>

**Example 3:**

<pre><code>Input: arr = [3,1,7,11]
<strong>Output:
</strong> false
<strong>Explanation:
</strong> In this case does not exist N and M, such that N = 2 * M.</code></pre>

&#x20;

**Constraints:**

* `2 <= arr.length <= 500`
* `-10^3 <= arr[i] <= 10^3`
