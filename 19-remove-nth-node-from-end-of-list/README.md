# 19. Remove Nth Node From End of List

## Medium

***

Given the `head` of a linked list, remove the `nth` node from the end of the list and return its head.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/03/remove\_ex1.jpg)

<pre><code>Input: head = [1,2,3,4,5], n = 2
<strong>Output:
</strong> [1,2,3,5]</code></pre>

**Example 2:**

<pre><code>Input: head = [1], n = 1
<strong>Output:
</strong> []</code></pre>

**Example 3:**

<pre><code>Input: head = [1,2], n = 1
<strong>Output:
</strong> [1]</code></pre>

&#x20;

**Constraints:**

* The number of nodes in the list is `sz`.
* `1 <= sz <= 30`
* `0 <= Node.val <= 100`
* `1 <= n <= sz`

&#x20;

**Follow up:** Could you do this in one pass?
