# Merge Two Sorted Lists

***

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists in a one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

Return _the head of the merged linked list_.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/03/merge\_ex1.jpg)

<pre><code>Input: list1 = [1,2,4], list2 = [1,3,4]
<strong>Output:
</strong> [1,1,2,3,4,4]</code></pre>

**Example 2:**

<pre><code>Input: list1 = [], list2 = []
<strong>Output:
</strong> []</code></pre>

**Example 3:**

<pre><code>Input: list1 = [], list2 = [0]
<strong>Output:
</strong> [0]</code></pre>

&#x20;

**Constraints:**

* The number of nodes in both lists is in the range `[0, 50]`.
* `-100 <= Node.val <= 100`
* Both `list1` and `list2` are sorted in **non-decreasing** order.
