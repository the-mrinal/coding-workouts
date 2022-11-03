# 1385. Find the Distance Value Between Two Arrays

## Easy

***

Given two integer arrays `arr1` and `arr2`, and the integer `d`, _return the distance value between the two arrays_.

The distance value is defined as the number of elements `arr1[i]` such that there is not any element `arr2[j]` where `|arr1[i]-arr2[j]| <= d`.

&#x20;

**Example 1:**

<pre><code>Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
<strong>Output:
</strong> 2
<strong>Explanation:
</strong> 
For arr1[0]=4 we have: 
|4-10|=6 > d=2 
|4-9|=5 > d=2 
|4-1|=3 > d=2 
|4-8|=4 > d=2 
For arr1[1]=5 we have: 
|5-10|=5 > d=2 
|5-9|=4 > d=2 
|5-1|=4 > d=2 
|5-8|=3 > d=2
For arr1[2]=8 we have:
<strong>|8-10|=2 &#x3C;= d=2
</strong>
<strong>|8-9|=1 &#x3C;= d=2
</strong>|8-1|=7 > d=2
<strong>|8-8|=0 &#x3C;= d=2
</strong></code></pre>

**Example 2:**

<pre><code>Input: arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
<strong>Output:
</strong> 2</code></pre>

**Example 3:**

<pre><code>Input: arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
<strong>Output:
</strong> 1</code></pre>

&#x20;

**Constraints:**

* `1 <= arr1.length, arr2.length <= 500`
* `-1000 <= arr1[i], arr2[j] <= 1000`
* `0 <= d <= 100`
