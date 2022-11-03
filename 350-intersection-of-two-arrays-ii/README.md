# 350. Intersection of Two Arrays II

## Easy

***

Given two integer arrays `nums1` and `nums2`, return _an array of their intersection_. Each element in the result must appear as many times as it shows in both arrays and you may return the result in **any order**.

&#x20;

**Example 1:**

<pre><code>Input: nums1 = [1,2,2,1], nums2 = [2,2]
<strong>Output:
</strong> [2,2]</code></pre>

**Example 2:**

<pre><code>Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
<strong>Output:
</strong> [4,9]
<strong>Explanation:
</strong> [9,4] is also accepted.</code></pre>

&#x20;

**Constraints:**

* `1 <= nums1.length, nums2.length <= 1000`
* `0 <= nums1[i], nums2[i] <= 1000`

&#x20;

**Follow up:**

* What if the given array is already sorted? How would you optimize your algorithm?
* What if `nums1`'s size is small compared to `nums2`'s size? Which algorithm is better?
* What if elements of `nums2` are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
