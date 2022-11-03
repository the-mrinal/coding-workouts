# 480. Sliding Window Median

## Hard

***

The **median** is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

* For examples, if `arr = [2,3,4]`, the median is `3`.
* For examples, if `arr = [1,2,3,4]`, the median is `(2 + 3) / 2 = 2.5`.

You are given an integer array `nums` and an integer `k`. There is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return _the median array for each window in the original array_. Answers within `10-5` of the actual value will be accepted.

&#x20;

**Example 1:**

<pre><code>Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
<strong>Output:
</strong> [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
<strong>Explanation:
</strong> 
Window position                Median
---------------                -----
[1  3  -1] -3  5  3  6  7        1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7        3
 1  3  -1  -3 [5  3  6] 7        5
 1  3  -1  -3  5 [3  6  7]       6</code></pre>

**Example 2:**

<pre><code>Input: nums = [1,2,3,4,2,3,1,4,2], k = 3
<strong>Output:
</strong> [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]</code></pre>

&#x20;

**Constraints:**

* `1 <= k <= nums.length <= 105`
* `-231 <= nums[i] <= 231 - 1`
