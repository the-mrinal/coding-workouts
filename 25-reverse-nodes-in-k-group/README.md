# 25. Reverse Nodes in k-Group

## Hard

***

Given the `head` of a linked list, reverse the nodes of the list `k` at a time, and return _the modified list_.

`k` is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of `k` then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/03/reverse\_ex1.jpg)

<pre><code>Input: head = [1,2,3,4,5], k = 2
<strong>Output:
</strong> [2,1,4,3,5]</code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/10/03/reverse\_ex2.jpg)

<pre><code>Input: head = [1,2,3,4,5], k = 3
<strong>Output:
</strong> [3,2,1,4,5]</code></pre>

&#x20;

**Constraints:**

* The number of nodes in the list is `n`.
* `1 <= k <= n <= 5000`
* `0 <= Node.val <= 1000`

&#x20;

**Follow-up:** Can you solve the problem in `O(1)` extra memory space?
